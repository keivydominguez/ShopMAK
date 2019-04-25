from tokenize import Token

from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django_filters import FilterSet
from django_filters import rest_framework as filters
from rest_framework.decorators import permission_classes, api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import *

@csrf_exempt
def Usuario_List(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return JsonResponse(serializer.data, safe=False)

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
def Usuario_Crear(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        #corregir
        serializer = FilterUsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class UsuarioFilter(FilterSet):
    is_active = filters.CharFilter('is_active')
    designation = filters.CharFilter('profile_designation')
    min_salasry = filters.CharFilter(method="filter_by_min_salary")
    max_salary = filters.CharFilter(method="filter_by_max_salary")

    class Meta:
        model = User
        fields = ('is_active', 'designation', 'username', )

    def filter_by_min_salary(self, queryset, name, value):
        queryset = queryset.filter(profile_salary_gt=value)
        return queryset
    def filter_by_max_salary(self, queryset, name, value):
        queryset = queryset.filter(profile_salary_lt=value)
        return queryset

class UsuarioListView(generics.ListAPIView):
    serializer_class = FilterUsuarioSerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = UsuarioFilter

    ordering_fields = ('is_active', 'username')
    ordering = ('username', )
    search_fields = ('username', 'first_name')

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return JsonResponse({'error': 'error '}, status=400)
    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({'error': 'error'}, status=404)
    dic = {
        "mensaje": "ok"
    }
    return JsonResponse(dic, status=200)