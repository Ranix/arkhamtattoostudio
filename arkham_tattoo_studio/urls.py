"""arkham_tattoo_studio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from web import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Web
    path('', views.home, name='home'),
    path('portafolio', views.portfolio, name='portfolio'),
    path('cotizar', views.CreateQuotation.as_view(), name='quotation'),
    path('agendar', views.CreateAppointment.as_view(), name='appointment'),
    path('contacto', views.contact, name='contact'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('change-password', auth_views.PasswordChangeView.as_view(), name='change_password'),

    # Quotation
    path('cotizaciones/', include('quotation.urls')),

    # Appointments
    path('citas/', include('appointments.urls')),

    # Payments
    path('pagos/', include('payments.urls')),

    # API
    path('api/', include('api.urls')),
]
