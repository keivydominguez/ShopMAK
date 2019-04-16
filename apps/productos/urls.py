from django.urls import path
from .import views

urlpatterns = [
    path('producto/', views.Producto_list),
    path('producto/<int:pk>/', views.Producto_detalle),
    path('whislist/', views.Whislist_List),
    path('whislist/<int:pk>/', views.Whislist_detalle),
]