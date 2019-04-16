from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *


@csrf_exempt
def Producto_list(request):
    if request.method == 'GET':
        producto = Productos.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
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
