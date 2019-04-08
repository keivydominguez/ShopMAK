from django.contrib import admin
from .models import Favorito, Categorias, Productos

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('Nombre_producto', 'Precio_producto', 'Usuario')

class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('Productos', 'Usuario')

admin.site.register(Productos, ProductosAdmin)

admin.site.register(Categorias)

admin.site.register(Favorito, FavoritoAdmin)

