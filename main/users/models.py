from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estados(models.Model):
    
    ESTADO_CHOICES = [
        ('pendiente','Pendiente'),
        ('en progreso','En Progreso'),
        ('completada','Completada')
    ]
    estado = models.CharField(max_length=30, choices=ESTADO_CHOICES)

    def __str__(self):
        return f'{self.estado}'
    
class Etiqueta(models.Model):
    ETIQUETA_CHOICES = [
        ('trabajo','Trabajo'),
        ('hogar','Hogar'),
        ('estudio','Estudio'),
    ]
    nombre_etiqueta = models.CharField(max_length=30, choices=ETIQUETA_CHOICES)
    
    def __str__(self):
        return f'{self.nombre_etiqueta}'

class Prioridades(models.Model):
    PRIORIDAD_CHOICES = [
        ('baja','Baja'),        
        ('media','Media'),        
        ('alta','Alta'),        
        ('critica','Critica'),        
    ]
    prioridad = models.CharField(max_length=40,choices=PRIORIDAD_CHOICES)
    
    def __str__(self):
        return f'PRIORIDAD {self.prioridad.upper()}'

class Tareas(models.Model):
    titulo = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=255)
    fecha_vencimiento = models.DateTimeField()
    estado = models.ForeignKey(Estados,on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta,on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    observacion = models.TextField(max_length=255, null=True)
    prioridad = models.ForeignKey(Prioridades,on_delete=models.PROTECT, null=True)
    def save(self,*args,**kwargs):
        if self.fecha_vencimiento and isinstance(self.fecha_vencimiento,str):
            self.fecha_vencimiento = datetime.strptime(self.fecha_vencimiento,"%d/%m/%Y %H:%M:%S")
        super().save(*args,**kwargs)

    def __str__(self):
        return f'TITULO: {self.titulo} DESCRIPCION: {self.descripcion} FECHA_VENCIMIENTO: {self.fecha_vencimiento} ESTADO: {self.estado} ETIQUETA: {self.etiqueta} USER: {self.usuario}'
    

    