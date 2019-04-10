from django.contrib import admin
from django.contrib.auth.models import Group
from .models import ComprasProducto, Compras, Pago

class PagoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['Productos', 'Envio', 'Total']}), ('Informacion de pago', {'fields': ['Nombre_tarjeta', 'Mes_tarjeta', 'año_tarjeta', 'CodigoSeg_Tarjeta', 'Numero_tarjeta']})
    ]

    list_display = ('Productos', 'Nombre_tarjeta', 'Total')

class ComprasAdmin(admin.ModelAdmin):
    list_display = ('Usuario', 'Fecha_compras')


admin.site.register(Pago, PagoAdmin)
admin.site.unregister(Group)

admin.site.register(Compras, ComprasAdmin)

admin.site.register(ComprasProducto)

