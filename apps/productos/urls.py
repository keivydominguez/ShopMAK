from django.urls import path
from .import views

urlpatterns = [
    path('get_all_products/', views.ProductoList.as_view()),
    path('get_WhisList/', views.WhisList.as_view()),
]