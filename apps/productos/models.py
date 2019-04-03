from django.db import models

class Categorias(models.Model):
    Nombre_categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

class Productos(models.Model):
    Nombre_producto = models.CharField(max_length=50)
    Marca_producto = models.CharField(max_length=15)
    Modelo_producto = models.CharField(max_length=50)
    Precio_producto = models.IntegerField(null=False, blank=True)