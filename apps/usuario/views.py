from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

@csrf_exempt
def Usuario_List(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def Usuario_detalle(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except usuario.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        usuario.delete()
        return HttpResponse(status=400)

@csrf_exempt
def Usuario_Login(request, pk):
    try:
        usuario = User.objects.get(pk=pk)
    except usuario.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LoginSerializer(usuario)
        return JsonResponse(serializer.data)

@csrf_exempt
def Usuario_Crear(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CrearUsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)