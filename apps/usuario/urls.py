from django.urls import path
from .import views

urlpatterns = [
    path('usuario/', views.index, name='index'),
]