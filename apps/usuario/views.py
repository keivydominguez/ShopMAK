from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


class LoginList(APIView):
    def post(self, request):
        usuarios = Usuario.objects.all()

        dic = {
            'usario': str(usuarios.Usario.username),
            'password': str(usuarios.Usario.password),
        }

        return Response(dic)

class UsuarioList(APIView):
    def post(self, request):
        usuario = Usuario.objects.all()

        dic ={
            'usuario': str(usuario.Usario.username),
            'nombre': str(usuario.Usario.first_name),
            'apellido': str(usuario.Usario.last_name),
            'correo': str(usuario.Usario.email),
            'telefono': usuario.Telefono,
            'calle': usuario.Calle,
            'colonia': usuario.Colonia,
            'codigopostal': usuario.CodigoPostal,
            'municipio': usuario.Municipio,
            'estado': usuario.Estado,
            'pais': usuario.Pais,

        }

        return Response(dic)