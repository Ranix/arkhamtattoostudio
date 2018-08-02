from django import forms

from web.models import Quotation

class CotizarAdminForm(forms.ModelForm):

    class Meta:
        model = Quotation

        fields = [
            'no_horas',
            'anticipo',
            'precioTotal',
            'comentarios',
            'correo',
        ]

        labels = {
            'no_horas' : 'Numero horas',
            'anticipo': 'Anticipo',
            'precioTotal' : 'Precio total',
            'comentarios' : 'Comentarios',
            'correo' : 'Correo',
        }

        widgets = {
            'no_horas' : forms.TextInput(attrs={'class':'form-control'}),
            'anticipo': forms.Select(attrs={'class':'form-control'}),
            'precioTotal': forms.TextInput(attrs={'class':'form-control'}),
            'comentarios': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            }
