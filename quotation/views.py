from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from web.models import Quotation
from quotation import forms


# Create your views here.
class CotizarList(LoginRequiredMixin, ListView):
    model = Quotation
    template_name = 'admin/cotizar_lista.html'


class CotizarUpdate(LoginRequiredMixin, UpdateView):
    model = Quotation
    form_class = forms.CotizarAdminForm
    template_name = 'admin/cotizar_form.html'
    success_url = reverse_lazy('cotizar_lista')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_cotizacion = kwargs['pk']
        cotizacion = self.model.objects.get(id=id_cotizacion)
        form = self.form_class(request.POST, instance=cotizacion)
        if form.is_valid():
            email = form.save(commit=False)
            email.cotizado = True
            email.save()
            subject = "Solicitud de cotizacion arkham tattoo studio"
            ctx = {
                'user_name': email.nombre,
                'zona': email.zona,
                'posicion': email.posicion,
                'colores': email.tinta,
                'alto': email.alto,
                'ancho': email.ancho,
                'descripcion':email.descripcion,
                'horas': email.no_horas,
                'anticipo': email.anticipo,
                'precio': email.precioTotal,
                'comentarios': email.comentarios,
            }
            message = get_template('email/email_cotizacion.html').render(ctx)
            to = [email.correo]
            from_email = 'arkhamcotizaciones@gmail.com'
            send_mail(subject, message, from_email, to, fail_silently=False, html_message=message)
            return HttpResponseRedirect(self.get_success_url())
        else:
            context = {'form': form}
            return render(request, self.template_name, context)


class CotizarDelete(LoginRequiredMixin, DeleteView):
    model = Quotation
    template_name = 'admin/cotizar_delete.html'
    success_url = reverse_lazy('cotizar_lista')
