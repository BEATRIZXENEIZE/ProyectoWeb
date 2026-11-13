from django.contrib import admin
from .models import Profesor

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni', 'legajo', 'especialidad', 'domicilio')
    search_fields = ('nombre', 'dni', 'legajo', 'especialidad')
