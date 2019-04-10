from django.db import models
from django.contrib.auth.models import User


class Categorias(models.Model):
    Nombre_categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre_categoria

class Productos(models.Model):
    Nombre_producto = models.CharField(max_length=50)
    Marca_producto = models.CharField(max_length=15)
    Modelo_producto = models.CharField(max_length=50)
    Precio_producto = models.FloatField()
    Cantidad_producto = models.IntegerField()
    Descripcion_producto = models.TextField()
    Foto_producto = models.CharField(max_length=50)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True, blank=True)
    Status_producto = models.CharField(max_length=45)

    def __str__(self):
        return self.Nombre_producto

class Favorito(models.Model):
    Productos = models.ForeignKey(Productos, on_delete=models.CASCADE, null=True, blank=True)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Productos.Nombre_producto