from django.contrib import admin
from .models import Perro, UsuarioAdoptante, #Adopcion


def mostrar_adoptante(perro):
    usuarios = UsuarioAdoptante.objects.filter(historial_adopciones=perro)
    if usuarios.exists():
        usuario = usuarios.first()
        return f"{usuario.nombre} {usuario.apellido}" 
    return "Sin adoptar"

mostrar_adoptante.short_description = 'Usuario Adoptante'

def mostrar_perros_adoptados(usuario):
    perros = usuario.historial_adopciones.all()
    return ", ".join([perro.nombre for perro in perros]) if perros else "Ninguno"

mostrar_perros_adoptados.short_description = 'Perros Adoptados'

@admin.register(Perro)
class PerroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'sexo', 'edad', 'peso', 'estado_salud', 'tamaño', 'vacunado', 'estado_adopcion', 'temperamento', mostrar_adoptante)
    search_fields = ('nombre', 'raza')
    list_filter = ('estado_salud', 'tamaño', 'estado_adopcion', 'temperamento')
    ordering = ('nombre',)
    list_per_page = 10

@admin.register(UsuarioAdoptante)
class UsuarioAdoptanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'email', 'telf', 'preferencias', mostrar_perros_adoptados)
    search_fields = ('nombre', 'apellido', 'dni')
    list_filter = ('preferencias',)
    ordering = ('apellido',)
    list_per_page = 10

#@admin.register(Adopcion)
#class AdopcionAdmin(admin.ModelAdmin):
#    list_display = ('adoptante', 'perro', 'estado_adopcion')
#    search_fields = ('adoptante__nombre', 'perro__nombre')


    