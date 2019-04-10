from .models import *
from rest_framework import serializers

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Productos
        fields=('id', 'Nombre_producto', 'Marca_producto', 'Modelo_producto', 'Precio_producto', 'Cantidad_producto',
                'Descripcion_producto', 'Foto_producto', 'Usuario', 'Categorias', 'Status_producto')
