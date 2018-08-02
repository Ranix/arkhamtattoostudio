from django.urls import path

from payments import views

urlpatterns = [
    path('', views.AgendarPagos.as_view(), name='pagos_lista'),
    #Report
    path('csv/', views.export_pagos_csv, name='export_pagos_csv'),
]
