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

#filter
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20, null=False, blank=False)
    salary = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('-salary',)

    def __str__(self):
        return "{0} - {1}".format(self.user.username, self.designation)


class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(profile__designation="Employee")


class Employee(User):
    class Meta:
        ordering = ("username",)
        proxy = True

    objects = EmployeeManager()

    def full_name(self):
        return self.first_name + " - " + self.last_name