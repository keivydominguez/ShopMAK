from django.urls import path

from apps.productos.views import SubirImagen
from .import views

urlpatterns = [
    path('producto/', views.Producto_list),
    path('producto/<int:pk>/', views.Producto_detalle),
    path('whislist/', views.Whislist_List),
    path('whislist/<int:pk>/', views.Whislist_detalle),
    path('imagenes/', views.SubirImagen),
]