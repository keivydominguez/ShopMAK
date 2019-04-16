from django.urls import path
from .import views

urlpatterns = [
    path('usuariolista/', views.Usuario_List),
    path('usuariolista/<int:pk>', views.Usuario_detalle),
    path('login/<int:pk>', views.Usuario_Login),
    path('Logincrear/', views.Usuario_Crear),
]