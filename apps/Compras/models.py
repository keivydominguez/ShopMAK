from django.db import models
from apps.productos.models import Productos
from django.contrib.auth.models import User

class Pago(models.Model):
    Productos = models.ForeignKey(Productos, on_delete=models.CASCADE, null=True, blank=True)
    Envio = models.FloatField()
    Total = models.FloatField()
    Nombre_tarjeta = models.CharField(max_length=100)
    Mes_tarjeta = models.CharField(max_length=2)
    año_tarjeta = models.CharField(max_length=2)
    CodigoSeg_Tarjeta = models.CharField(max_length=3)
    Numero_tarjeta = models.CharField(max_length=16)

    def __str__(self):
        return self.Nombre_tarjeta

class Compras(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Pago = models.ForeignKey(Pago, on_delete=models.CASCADE, null=True, blank=True)
    Fecha_compras = models.DateField()

    def __str__(self):
        return self.Usuario.USERNAME_FIELD

class ComprasProducto(models.Model):
    Productos = models.ForeignKey(Productos, on_delete=models.CASCADE, null=True, blank=True)
    Compras = models.ForeignKey(Compras, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Productos.Nombre_producto
