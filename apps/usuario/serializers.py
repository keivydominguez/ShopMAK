from django.forms import CharField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('Usario', 'Telefono', 'Calle', 'Colonia', 'CodigoPostal', 'Municipio', 'Estado', 'Pais')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['salary', 'designation', 'picture']
class FilterUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name',
                'last_name', 'profile', 'email',
                'is_staff', 'is_active', 'date_joined',
                'is_superuser')