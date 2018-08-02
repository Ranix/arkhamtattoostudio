from django.urls import path

from quotation import views

urlpatterns = [
    path('', views.CotizarList.as_view(), name='cotizar_lista'),
    path('editar/<int:pk>/', views.CotizarUpdate.as_view(), name='cotizar_editar'),
    path('eliminar/<int:pk>/', views.CotizarDelete.as_view(), name='cotizar_delete'),
]
