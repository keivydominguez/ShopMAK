from django.contrib.auth import login
from django.urls import path

from apps.usuario.views import UsuarioListView
from .import views

urlpatterns = [
    path('usuariolista/', views.Usuario_List),
    path('usuariolista/<int:pk>/', views.Usuario_detalle),
    path('Logincrear/', views.Usuario_Crear),
    path('filter/', UsuarioListView.as_view()),
]