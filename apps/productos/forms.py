from django import forms
from .models import *

class ProductoForm(forms.ModelForm):
    class Meta:
        model= Productos
        fields = ("Nombre_producto", "Marca_producto", "Modelo_producto", "Precio_producto", "Cantidad_producto", "Descripcion_producto",
                  "Usuario", "Categorias", "Status_producto" )