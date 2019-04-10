from django.http import HttpResponse, response
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *


class ProductoList(APIView):
    def post(self, request, *args, **kwargs):
        Producto = Productos.objects.all()
        list = []

        for data in Producto:
            list.append({
                "id": data.id,
                "nombre_producto": data.Nombre_producto,
                "marca": data.Marca_producto,
                "modelo": data.Modelo_producto,
                "precio": data.Precio_producto,
                "cantidad": data.Cantidad_producto,
                "descripcion": data.Descripcion_producto,
                "foto": data.Foto_producto,
                "nombre_usuario": str(data.Usuario.username),
                "categoria": str(data.Categorias.Nombre_categoria),
                "status": data.Status_producto,
            })

        return Response(list)


class WhisList(APIView):
    def post(self, request, *args, **kwargs):
        whislist = Favorito.objects.all()
        list = []

        for data in whislist:
            list.append({
                "id": data.id,
                "id_producto": str(data.Productos.id),
                "nombre_producto": str(data.Productos.Nombre_producto),
                "descripcion": str(data.Productos.Descripcion_producto),
                "foto": str(data.Productos.Foto_producto),
                "precio": str(data.Productos.Precio_producto),
                "id_usuario": str(data.Usuario.id),

            })

        return Response(list)
