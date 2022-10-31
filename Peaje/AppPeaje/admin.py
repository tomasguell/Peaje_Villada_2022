from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header='PEAJE'
admin.site.index_title = 'ADMIN PEAJE'
admin.site.site_title='PEAJE'

class OperadoresAdmin(admin.ModelAdmin):
    list_display =['numeroEmpleado','nombre','apellido','numeroDocumento','tipoDocumento'] 
    search_fields=['numeroEmpleado']
    list_filter=('numeroEmpleado','apellido','nombre')

admin.site.register(operadores, OperadoresAdmin)
admin.site.register(rutas)

class EstacionesAdmin(admin.ModelAdmin):
    list_display =['nombre','km','ruta'] 
    search_fields=['ruta']
admin.site.register(estaciones,EstacionesAdmin)
admin.site.register(TipoDocumento)

admin.site.register(casillas)
admin.site.register(tipoVehiculo)

class TicketAdmin(admin.ModelAdmin):
    list_display =['importe','fecha','hora','tipoVehiculo'] 
    list_filter=('importe','fecha','hota','tipoVehiculo')
admin.site.register(ticket)


admin.site.register(turnos)

