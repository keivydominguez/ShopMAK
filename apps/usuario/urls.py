from django.urls import path
from .import views

urlpatterns = [
    path('get_login/', views.LoginList.as_view()),
    path('get_usuario/', views.UsuarioList.as_view()),
]