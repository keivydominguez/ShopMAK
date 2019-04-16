from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

@csrf_exempt
def Pago_List(request):
    if request.method == 'GET':
        pago = Pago.objects.all()
        serializer = PagoSerializer(pago, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PagoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def Pago_Borrar(request, pk):
    try:
        pago = Pago.objects.get(pk=pk)
    except pago.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        pago.delete()
        dic = {
            'mensaje', "Se borro con exito"
        }
        return HttpResponse(dic)

@csrf_exempt
def Compra_List(request):
    if request.method == 'GET':
        compras = Compras.objects.all()
        serializer = CompraSerializer(compras, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def Compras_detalle(request, pk):
    try:
        compras = Compras.objects.get(pk=pk)
    except compras.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CompraSerializer(compras)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CompraSerializer(compras, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        compras.delete()
        return HttpResponse(status=400)
