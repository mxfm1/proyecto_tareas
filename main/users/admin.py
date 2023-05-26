from django.contrib import admin
from .models import Tareas, Estados,Etiqueta, Prioridades
# Register your models here.


admin.site.register(Tareas)
admin.site.register(Estados)
admin.site.register(Etiqueta)
admin.site.register(Prioridades)