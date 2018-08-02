import csv

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now
from django.views.generic import ListView

from web.models import Payment

# Create your views here.
class AgendarPagos(ListView):
    model = Payment
    template_name = 'admin/pagos.html'

    def get_queryset(self):
        return Payment.objects.filter(fecha__month=now().month)


def export_pagos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pagos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Tipo Pago', 'Fecha de pago', 'Cliente', 'Cantidad'])

    pagos = Payment.objects.filter(fecha__month=now().month)
    for pago in pagos:
        writer.writerow([pago.fecha, pago.tipo_pago, pago.tipo_pago, pago.cita.cliente.nombre, pago.cantidad])
    return response
