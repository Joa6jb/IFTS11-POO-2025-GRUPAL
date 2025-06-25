from django.contrib import admin
from .models import Perro, UsuarioAdoptante, Adopcion

@admin.register(Perro)
class PerroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'sexo', 'edad', 'peso', 'estado_salud', 'tamaño', 'vacunado', 'estado_adopcion', 'temperamento')
    search_fields = ('nombre', 'raza')
    list_filter = ('estado_salud', 'tamaño', 'estado_adopcion', 'temperamento')
    ordering = ('nombre',)
    list_per_page = 10

@admin.register(UsuarioAdoptante)
class UsuarioAdoptanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'email', 'telf', 'pref_raza', 'pref_edad', 'pref_tamaño')
    search_fields = ('nombre', 'apellido', 'dni')
    list_filter = ('pref_raza', 'pref_edad', 'pref_tamaño')
    ordering = ('apellido',)
    list_per_page = 10

@admin.register(Adopcion)
class AdopcionAdmin(admin.ModelAdmin):
    list_display = ('adoptante', 'perro', 'estado_adopcion')
    search_fields = ('adoptante__nombre', 'perro__nombre')
