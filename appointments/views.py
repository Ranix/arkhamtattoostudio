from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, UpdateView, DeleteView

from web.models import Appointment

# Create your views here.
class AgendarList(ListView):
    model = Appointment
    template_name = 'admin/agendar_lista.html'

    def get_queryset(self):
        return Appointment.objects.filter(dia__day=now().day)


class AgendarListM(ListView):
    model = Appointment
    template_name = 'admin/agendar_lista_m.html'

    def get_queryset(self):
        return Appointment.objects.filter(dia__month=now().month)


class AgendarDelete(DeleteView):
    model = Appointment
    template_name = 'admin/agendar_delete.html'
    success_url = reverse_lazy('cita_lista_d')


# class AgendarUpdate(UpdateView):
#     model = Appointment
#     form_class = forms.AgendarClienteForm
#     template_name = 'admin/cotizar_form.html'
#     success_url = reverse_lazy('cotizar_lista')
