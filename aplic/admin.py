from django.contrib import admin
from aplic.models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display=('id','identificacion','razonSocial','nombres','apellidos')
    
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Factura)
admin.site.register(DetFactura)
admin.site.register(Producto)
admin.site.register(Empresa)
admin.site.register(Parametro)
admin.site.register(ValorParametro)