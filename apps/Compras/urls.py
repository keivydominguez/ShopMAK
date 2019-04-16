from django.urls import path
from .import views

urlpatterns = [
    path('pago/', views.Pago_List),
    path('pago/<int:pk>/', views.Pago_Borrar),
    path('compra/', views.Compra_List),
    path('compra/<int:pk>/', views.Compras_detalle),
]