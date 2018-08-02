import calendar

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.utils.timezone import now
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView

from web.models import Quotation, Client, Appointment, Payment
from web import forms

# Web views.
def home(request):
    return render(request, 'web/index.html')

def portfolio(request):
    return render(request, 'web/portafolio.html')

def contact(request):
    return render(request, 'web/contacto.html')

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
        #Calendar
        month_name = calendar.month_name[now().month]
        cal = calendar.Calendar()
        cal.setfirstweekday(6) #firstweekday = Sunday = 6
        month = [[]]
        week = 0
        month_events = Appointment.objects.filter(dia__year=now().year).filter(dia__month=now().month)
        for day in cal.itermonthdays(now().year, now().month):
            if day:
                occurrences = list(filter(lambda e: e.dia.day==day, month_events))
            else:
                occurrences = []
            month[week].append((day, occurrences))
            if len(month[week]) == 7:
                    month.append([])
                    week += 1
        context.update({'year': now().year, 'month_name': month_name, 'month': month})
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
            '''
            subject = "Recibo de pago arkham tattoo studio"
            ctx = {
                'user_name': cliente.nombre,
                'dia' : cita.dia,
                'tipo' : pago.tipo_pago,
                'anticipo': pago.cantidad,
            }
            message = get_template('email/email_recibo.html').render(ctx)
            to = [cliente.correo]
            from_email = 'arkhamcotizaciones@gmail.com'
            send_mail(subject, message, from_email, to, fail_silently=False, html_message=message)
            '''
            messages.add_message(request, messages.INFO, 'Su cita se a creado exitosamente')
            return HttpResponseRedirect(self.get_success_url())
        else:
            print('no es valido')
            context = {
                'form': form,
                'form2': form2,
                'form3': form3
            }
            return render(request, self.template_name, context)
