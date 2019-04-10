from django.urls import path
from .import views

urlpatterns = [
    path('get_compras/', views.ComprasList.as_view()),
]