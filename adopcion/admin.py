from django.contrib import admin
from .models import Adopcion
from contacto.models import Contacto

# Register your models here.

class AdopcionAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Adopcion, AdopcionAdmin)
admin.site.register(Contacto)
