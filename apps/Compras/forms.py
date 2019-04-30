from django import forms
from .models import *

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ("Productos", "Envio", "Total", "Nombre_tarjeta", "Mes_tarjeta", "año_tarjeta", "CodigoSeg_Tarjeta", "Numero_tarjeta")

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ("Usuario", "Pago", "Fecha_compras")