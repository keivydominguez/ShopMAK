from _elementtree import ParseError

from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, parsers, viewsets
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from .models import *
from .serializers import *


@csrf_exempt
def Producto_list(request):
    if request.method == 'GET':
        producto = Productos.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        dic = {
            "id": request.POST['id'],
            "Nombre_producto": request.POST['Nombre_producto'],
            "Marca_producto": request.POST['Marca_producto'],
            'Modelo_producto': request.POST['Modelo_producto'],
            'Precio_producto': request.POST['Precio_producto'],
            'Cantidad_producto': request.POST['Cantidad_producto'],
            'Descripcion_producto': request.POST['Descripcion_producto'],
            'Usuario': request.POST['Usuario'],
            'Categorias': request.POST['Categorias'],
            'Status_producto': request.POST['Status_producto'],
        }
        #data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=dic)
        if serializer.is_valid():
            serializer.save()
            #print(serializer.data["id"])
            #aqui subes las imagenes
            nuevoProducto = Productos.objects.get(pk=serializer.data["id"])
            new_img=Imagenes()
            new_img.producto_id=nuevoProducto
            new_img.imagen=request.FILES['img']
            new_img.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def Producto_detalle(request, pk):
    try:
        producto = Productos.objects.get(pk=pk)
    except producto.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser(). parse(request)
        serializer = ProductoSerializer(producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        producto.delete()
        dic = {
            'mensaje': "Se borro con exito"
        }
        return HttpResponse(dic)

@csrf_exempt
def Whislist_List(request):
    if request.method == 'GET':
        favorito = Favorito.objects.all()
        serializer = WhislistSerializer(favorito, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WhislistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def Whislist_detalle(request, pk):
    try:
        favoritos = Favorito.objects.get(pk=pk)
    except favoritos.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = WhislistSerializer(favoritos)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser(). parse(request)
        serializer = WhislistSerializer(favoritos, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        favoritos.delete()
        dic = {
            'mensaje': "Se borro con exito"
        }
        return HttpResponse(dic)
