from django import forms

from web.models import Quotation, Client, Appointment, Payment

# Cotizacion Forms.
class QuotationForm(forms.ModelForm):

    class Meta:
        model = Quotation
        fields = [
            'nombre',
            'telefono',
            'correo',
            'zona',
            'posicion',
            'tinta',
            'alto',
            'ancho',
            'referencia1',
            'referencia2',
            'referencia3',
            'descripcion',
            'cotizado',
        ]

        labels = {
            'nombre' : 'Nombre:',
            'telefono' : 'Teléfono:',
            'correo' : 'Correo electrónico:',
            'zona' : 'Zona a tatuar:',
            'posicion': 'Frente o Posterior:',
            'tinta' : 'Colores:',
            'alto' : 'Alto:',
            'ancho' : 'Ancho:',
            'referencia1' : 'Referencia1:',
            'referencia2' : 'Referencia2:',
            'referencia3' : 'Referencia3:',
            'descripcion': 'Descripción del tatuaje:',
        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'caja'}),
            'telefono' : forms.TextInput(attrs={'class':'caja'}),
            'correo' : forms.TextInput(attrs={'class':'caja'}),
            'zona' : forms.Select(attrs={'class':'caja'}),
            'posicion' : forms.Select(attrs={'class':'caja'}),
            'tinta' : forms.Select(attrs={'class':'caja'}),
            'alto' : forms.TextInput(attrs={'class':'caja5'}),
            'ancho' : forms.TextInput(attrs={'class':'caja5'}),
            'descripcion' : forms.TextInput(attrs={'class':'caja2'}),
            }


# Agendar Forms
class AgendarClienteForm(forms.ModelForm):

    class Meta:
        model = Client

        fields = [
            'nombre',
            'edad',
            'telefono',
            'correo',
        ]

        labels = {
            'nombre' : 'Nombre:',
            'edad' : 'Edad:',
            'telefono' : 'Teléfono:',
            'correo' : 'Correo electrónico:',
        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'caja'}),
            'edad' : forms.TextInput(attrs={'class':'caja'}),
            'telefono' : forms.TextInput(attrs={'class':'caja'}),
            'correo' : forms.TextInput(attrs={'class':'caja'}),
        }


class AgendarCitaForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            'descripcion',
            'dia',
            'start',
            'end',
        ]

        widgets = {
            'descripcion' : forms.TextInput(attrs={'class':'caja'}),
            #'no_horas': forms.Select(attrs={'class':'caja'})
        }

class AgendarPagoForm(forms.ModelForm):

    class Meta:
        model = Payment

        fields = [
            'tipo_pago',
            'cantidad',
        ]

        widgets = {
            'tipo_pago': forms.Select(attrs={'class':'caja'}),
            'cantidad' : forms.TextInput(attrs={'class':'caja'})
        }

# class CotizarAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = Cotizacion
#
#         fields = [
#             'no_horas',
#             'anticipo',
#             'precioTotal',
#             'comentarios',
#             'correo',
#         ]
#
#         labels = {
#             'no_horas' : 'Numero horas',
#             'anticipo': 'Anticipo',
#             'precioTotal' : 'Precio total',
#             'comentarios' : 'Comentarios',
#             'correo' : 'Correo',
#         }
#
#         widgets = {
#             'no_horas' : forms.TextInput(attrs={'class':'form-control'}),
#             'anticipo': forms.Select(attrs={'class':'form-control'}),
#             'precioTotal': forms.TextInput(attrs={'class':'form-control'}),
#             'comentarios': forms.TextInput(attrs={'class':'form-control'}),
#             'correo': forms.TextInput(attrs={'class':'form-control'}),
#             }
