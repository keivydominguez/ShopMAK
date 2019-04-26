from django.urls import path

from apps.productos.views import ProductotView
from .import views

urlpatterns = [
    path('producto/', views.Producto_list),
    path('producto/<int:pk>/', views.Producto_detalle),
    path('whislist/', views.Whislist_List),
    path('whislist/<int:pk>/', views.Whislist_detalle),
    path('index/back/', ProductotView.as_view(), name='producto'),
    path('index/back/borrar/<pk>', views.borrar_producto, name='borrar'),
    path('index/back/editar/<pk>', views.editar_producto, name='editar'),
]