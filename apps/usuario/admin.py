from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('Usario', 'Telefono')

admin.site.register(Usuario, UsuarioAdmin)


