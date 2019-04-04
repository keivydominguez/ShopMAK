from django.db import models
from apps.productos.models import Productos
from django.contrib.auth.models import User

class Pago(models.Model):
    Productos = models.ForeignKey(Productos, on_delete=models.CASCADE, null=True, blank=True)
    Envio = models.IntegerField(null=False, blank=True)
    Total = models.FloatField(null=False, blank=True)
    Nombre_tarjeta = models.CharField(max_length=100)
    Mes_tarjeta = models.IntegerField(max_length=2)
    año_tarjeta = models.IntegerField(max_length=2)
    CodigoSeg_Tarjeta = models.IntegerField(max_length=3)
    Numero_tarjeta = models.IntegerField(max_length=16)

    def __str__(self):
        return self.Nombre_tarjeta

class Compras(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Pago = models.ForeignKey(Pago, on_delete=models.CASCADE, null=True, blank=True)
    Fecha_compras = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Pago
