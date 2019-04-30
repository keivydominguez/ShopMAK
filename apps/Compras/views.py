from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from .forms import *

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

#backofice
class PagoView(ListView):
    model = Pago
    template_name = "../templates/pago.html"

def pago(request):
    pago = Pago.objects.all()
    dic = {
        "lista": pago
    }
    return render(request, '../templates/pago.html', dic)

def borrar_pago(request, pk):
    borrar = Pago.objects.get(pk=pk)
    borrar.delete()
    return HttpResponseRedirect('/pago/back/')

def editar_pago(request, pk):
    if request.method == 'POST':
        pago = Pago.objects.get(pk=pk)
        pagoform = PagoForm(request.POST, instance=pago)
        if pagoform.is_valid():
            pagoform.save()
            return HttpResponseRedirect('/pago/back/')
    else:
        pago = Pago.objects.get(pk=pk)
        pagoform = PagoForm(instance=pago)

        dic = {
            "pagoform": pagoform
        }
        return render(request, '../templates/FormPago.html', dic)

class CompraView(ListView):
    model = Compras
    template_name = '../templates/compra.html'

def compra(request):
    compra = Compras.objects.all()
    dic = {
        "list": compra
    }
    return render(request, '../templates/compra.html', dic)

def borrar_compra(request, pk):
    borrar = Compras.objects.get(pk=pk)
    borrar.delete()
    return HttpResponseRedirect('/compra/back/')

def editar_compra(request, pk):
    if request.method == 'POST':
        compra = Compras.objects.get(pk=pk)
        compraform = CompraForm(request.POST, instance=compra)
        if compraform.is_valid():
            compraform.save()
            return HttpResponseRedirect('/compra/back/')
    else:
        compra = Compras.objects.get(pk=pk)
        compraform = CompraForm(instance=compra)
        dic = {
            "compraform": compraform
        }
        return render(request, '../templates/FormCompra.html', dic)