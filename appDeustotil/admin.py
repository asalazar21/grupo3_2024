from django.contrib import admin
from .models import Proyecto, Tarea, Empleado, Cliente, EstadoTarea, Prioridad
admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(EstadoTarea)
admin.site.register(Prioridad)