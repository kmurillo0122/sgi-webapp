from django.contrib import admin
from .models import UsuariosSena, Elementos, Prestamo
from .choices import roles, cuentadantes

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(UsuariosSena)
admin.site.register(Elementos)
admin.site.register(Prestamo)