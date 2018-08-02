from django.contrib import admin
from .models import Quotation, Client, Appointment, Payment

# Register your models here.
admin.site.register(Quotation)
admin.site.register(Client)
admin.site.register(Appointment)
admin.site.register(Payment)
