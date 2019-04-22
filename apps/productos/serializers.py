from rest_framework import serializers
from .models import *

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ('id', 'Nombre_producto', 'Marca_producto', 'Modelo_producto', 'Precio_producto',
                  'Cantidad_producto', 'Descripcion_producto', 'Usuario', 'Categorias', 'Status_producto')

class WhislistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = ('id', 'Productos', 'Usuario')

class ImageneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = [
            'producto_id',
            'imagen'
        ]
    def create(self, validated_data):
        return Imagenes.objects.create(**validated_data)