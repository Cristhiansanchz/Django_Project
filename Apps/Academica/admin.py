from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Nivel_Educativo)
class NivelEducativoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nivel_educativo')

@admin.register(Modalidad)
class ModalidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Territorial)
class TerritorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Cetap)
class CetapAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'territorial')

@admin.register(Egresado)
class EgresadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'cedula', 'email_personal', 'email_institucional', 'celular', 'fecha_grado', 'nivel_educativo', 'titulo', 'modalidad', 'territorial', 'cetap', 'active', 'created_at', 'update_at')

