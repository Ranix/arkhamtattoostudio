import calendar
from datetime import date, time, datetime, timedelta

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.utils.timezone import now
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView

from web.models import Quotation, Client, Appointment, Payment
from web import forms

from api.views import FreeHours


# Web views.
def home(request):
    return render(request, 'web/index.html')


def portfolio(request):
    return render(request, 'web/portafolio.html')


def contact(request):
    if request.method == 'GET':
        form = forms.ContactForm()
    else:
        form = forms.ContactForm(request.POST)
        print(form)
        if form.is_valid():
            subject = 'Test de errores en pagina'
            message = form.cleaned_data['message']
            from_email = 'arkhamcotizaciones@gmail.com'
            try:
                send_mail(subject, message, from_email, ['ale.manriquezr@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "web/contacto.html", {'form': form})
    return render(request, "web/contacto.html", {'form': form})


class CreateQuotation(SuccessMessageMixin, CreateView):
    model = Quotation
    form_class = forms.QuotationForm
    template_name = 'web/cotizar.html'
    success_url = reverse_lazy('quotation')
    success_message = "Cotizacion creada exitosamente"


class CreateAppointment(SuccessMessageMixin, CreateView):
    model = Client
    second_model = Appointment
    third_model = Payment
    form_class = forms.AgendarClienteForm
    second_form_class = forms.AgendarCitaForm
    third_form_class = forms.AgendarPagoForm
    template_name = 'web/agendar.html'
    success_url = reverse_lazy('appointment')

    def get_context_data(self, **kwargs):
        context = super(CreateAppointment, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        # Calendar
        # month_name = calendar.month_name[now().month]
        month_name = {
            1: "Enero",
            2: "Febrero",
            3: "Marzo",
            4: "Abril",
            5: "Mayo",
            6: "Junio",
            7: "Julio",
            8: "Agosto",
            9: "Septiembre",
            10: "Octubre",
            11: "Noviembre",
            12: "Diciembre",
        }
        cal = calendar.Calendar()
        cal.setfirstweekday(6)# firstweekday = Sunday = 6
        month = [[]]
        week = 0
        month_events = Appointment.objects.filter(dia__year=now().year).filter(dia__month=now().month)
        for day in cal.itermonthdays(now().year, now().month):
            if day:
                occurrences = list(filter(lambda e: e.dia.day==day, month_events))
                #
                import pytz
                utc = pytz.UTC
                appointments = []
                for event in occurrences:
                    start_date = datetime.combine(event.dia, event.start)
                    start_date = utc.localize(start_date)
                    end_date = datetime.combine(event.dia, event.end)
                    end_date = utc.localize(end_date)
                    appointments.append((start_date, end_date))
                work_hours = (datetime(int(now().year), int(now().month), int(day), 11, tzinfo=utc),
                        datetime(int(now().year), int(now().month), int(day), 18, tzinfo=utc))
                work_intervals = timedelta(minutes=30)
                slots = sorted([(work_hours[0], work_hours[0])] + appointments + [(work_hours[1], work_hours[1])])
                free_hours = []
                for start, end in ((slots[i][1], slots[i+1][0]) for i in range(len(slots)-1)):
                    assert start <= end, "Cannot attend all appointments"
                    while start + work_intervals <= end:
                        free_hours.append("{:%H:%M}".format(start))
                        start += work_intervals
                count = len(free_hours)
            else:
                occurrences = []
                count = 0
            # month[week].append((day, occurrences))
            month[week].append((day, count))
            if len(month[week]) == 7:
                    month.append([])
                    week += 1
        context.update({'year': now().year, 'month_name': month_name[now().month], 'month': month})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            cita = form2.save(commit=False)
            cita.cliente_id = cliente.id
            cita.save()
            pago = form3.save(commit=False)
            pago.cita_id = cita.id
            pago.save()
            subject = "Recibo de pago arkham tattoo studio"
            ctx = {
                'user_name': cliente.nombre,
                'dia': cita.dia,
                'inicia': cita.start,
                'termina': cita.end,
                'tipo': pago.tipo_pago,
                'anticipo': pago.cantidad,
            }
            message = get_template('email/email_recibo.html').render(ctx)
            to = [cliente.correo]
            from_email = 'arkhamcotizaciones@gmail.com'
            send_mail(subject, message, from_email, to, fail_silently=False, html_message=message)
            messages.add_message(request, messages.INFO, 'Su cita se a creado exitosamente')
            return HttpResponseRedirect(self.get_success_url())
        else:
            context = {
                'form': form,
                'form2': form2,
                'form3': form3
            }
            return render(request, self.template_name, context)
