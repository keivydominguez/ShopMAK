import json

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from rest_framework.parsers import JSONParser
from .serializers import *
from .forms import *
#192.168.2.106
#API
@csrf_exempt
def Producto_list(request):
    if request.method == 'GET':
        producto = Productos.objects.all()
        lista = []
        for foo in producto:
            ProdDic = {
                "id": foo.id,
                "Nombre_producto": foo.Nombre_producto,
                "Marca_producto": foo.Marca_producto,
                "Modelo_producto": foo.Modelo_producto,
                "Precio_producto": foo.Precio_producto,
                "Cantidad_producto": foo.Cantidad_producto,
                "Descripcion_producto": foo.Descripcion_producto,
                "Usuario": str(foo.Usuario),
                "Categorias": str(foo.Categorias),
                "Status_producto": foo.Status_producto,
                "img": [
                    "https://picsum.photos/id/617/200/300?grayscale",
                    "https://picsum.photos/id/617/200/300?grayscale",
                    "https://picsum.photos/id/617/200/300?grayscale",
                    "https://picsum.photos/id/617/200/300?grayscale"
                ]
            }
            ProdDic = json.dumps(ProdDic)
            print(ProdDic)
        return JsonResponse(ProdDic, content_type='application/json')
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

#backofice
class ProductotView(ListView):
    model = Productos
    template_name = "../templates/producto.html"

def producto(request):
    Producto = Productos.objects.all()
    dic = {
        "lista": producto,
    }
    return render(request, '../templates/producto.html', dic)

def borrar_producto(request, pk):
    borrar = Productos.objects.get(pk=pk)
    borrar.delete()
    return HttpResponseRedirect('/index/back/')

def editar_producto(request, pk):
    if request.method == "POST":
        producto = Productos.objects.get(pk=pk)
        productoForm = ProductoForm(request.POST, instance=producto)
        if productoForm.is_valid():
            productoForm.save()
            return HttpResponseRedirect('/index/back/')
    else:
        producto = Productos.objects.get(pk=pk)
        productoForm = ProductoForm(instance=producto)

        dic = {
            "productoForm" : productoForm
        }
        return render(request, '../templates/FormProducto.html', dic)