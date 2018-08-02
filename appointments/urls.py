from django.urls import path

from appointments import views

urlpatterns = [
    path('',views.AgendarList.as_view(), name='cita_lista_d'),
    path('mes/', views.AgendarListM.as_view(), name='cita_lista_m'),
    path('eliminar/<int:pk>/', views.AgendarDelete.as_view(), name='cita_delete')
]
