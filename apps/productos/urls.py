from django.urls import path
from .import views

urlpatterns = [
    path('producto/', views.Producto_list),
]