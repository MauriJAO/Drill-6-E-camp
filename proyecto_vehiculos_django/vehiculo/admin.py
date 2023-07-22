from django.contrib import admin
from .models import VehiculoModel

# Register your models here.



@admin.register(VehiculoModel)
class Vehiculoadmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "serial_carroceria", "serial_motor", "categoria", "precio")
