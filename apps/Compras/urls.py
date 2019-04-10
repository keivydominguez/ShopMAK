from django.urls import path
from .import views

urlpatterns = [
    path('compras/', views.index, name='index'),
]