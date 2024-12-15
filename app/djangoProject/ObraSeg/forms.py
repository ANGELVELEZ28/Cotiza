from django import forms
from ObraSeg.models import Cotizador

class CotizadorForm(forms.ModelForm):
    class Meta:
        model = Cotizador
        fields = '__all__'  # Incluimos todos los campos del modelo Cotizador
        widgets = {
            'date_cotiza': forms.DateInput(attrs={'type': 'date'}),
            'comments': forms.Textarea(attrs={'rows': 4}),
            'state': forms.Select(attrs={'class': 'form-select'}),
        }