from django.urls import path
from .import views

urlpatterns = [
    path('producto/', views.index, name='index'),
]