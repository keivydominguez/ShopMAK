from django.contrib.auth import login
from django.urls import path

from apps.usuario.views import UsuarioListView, UsarioView
from .import views

urlpatterns = [
    path('usuariolista/', views.Usuario_List),
    path('usuariolista/<int:pk>/', views.Usuario_detalle),
    path('Logincrear/', views.Usuario_Crear),
    path('filter/', UsuarioListView.as_view()),
    path('Login/', views.login),
    path('usuario/back/', UsarioView.as_view(), name='Usuario'),
    path('usuario/back/editar/<pk>', views.editar_usuario, name='usuario_editar'),
    path('usuario/back/borrar/<pk>', views.borrar_usuario, name='usuario_borrar'),
]