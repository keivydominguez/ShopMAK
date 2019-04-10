from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


class ComprasList(APIView):
    def post(self, request):
        compras = Compras.objects.all()
        list = []

        for data in compras:
            list.append({
                "id": data.id,
                "nombre_usuario": str(data.Usuario.username),
                "nombre_producto": str(data.Pago.Productos.Nombre_producto),
                "descripcion": str(data.Pago.Productos.Descripcion_producto),
                "precio": str(data.Pago.Productos.Precio_producto),
                "foto": str(data.Pago.Productos.Foto_producto),
                "fecha": data.Fecha_compras,
            })


        return Response(list)