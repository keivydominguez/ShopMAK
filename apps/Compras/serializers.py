from rest_framework import serializers
from .models import *

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ('id', 'Productos', 'Envio', 'Total', 'Nombre_tarjeta', 'Mes_tarjeta', 'año_tarjeta', 'CodigoSeg_Tarjeta', 'Numero_tarjeta')

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = ('id', 'Usuario', 'Pago', 'Fecha_compras')