from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    Usario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    Telefono = models.CharField(max_length=16)
    Calle = models.CharField(max_length=50)
    Colonia = models.CharField(max_length=50)
    CodigoPostal = models.CharField(max_length=5)
    Municipio = models.CharField(max_length=50)
    Estado = models.CharField(max_length=50)
    Pais = models.CharField(max_length=20)

    def __str__(self):
        return self.Usario.USERNAME_FIELD