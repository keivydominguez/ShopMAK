from django.urls import path
from apps.Compras.views import *
from .import views

urlpatterns = [
    path('pago/', views.Pago_List),
    path('pago/<int:pk>/', views.Pago_Borrar),
    path('compra/', views.Compra_List),
    path('compra/<int:pk>/', views.Compras_detalle),
    path('pago/back/', PagoView.as_view(), name='pago'),
    path('pago/back/borrar/<pk>', views.borrar_pago, name='borrar_pago'),
    path('pago/back/editar/<pk>', views.editar_pago, name='editar_pago'),
    path('compra/back/', CompraView.as_view(), name='compra'),
]