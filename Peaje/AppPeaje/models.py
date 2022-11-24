from secrets import choice
from statistics import mode
from tkinter import CASCADE
from django.db import models
from .tipoDocumento import documento
from .sentido import sentido
from .tipoVehiculo import tipo
from .horarios import horario
from django.utils import timezone

# Create your models here.
class TipoDocumento(models.Model):
    tipo=models.CharField(max_length=30, choices=documento,default='DNI')
    descripcion=models.CharField(max_length=100)
    def __str__(self):
        return self.tipo



class operadores(models.Model):
    numeroEmpleado=models.CharField(max_length=10)
    numeroDocumento=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    tipoDocumento=models.ForeignKey(TipoDocumento,on_delete=models.CASCADE)
    def __str__(self):
        return (f'{self.nombre} - {self.apellido}')

class rutas(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class estaciones(models.Model):
    km= models.CharField(max_length=3)
    nombre=models.CharField(max_length=30)
    ruta=models.ForeignKey(rutas, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class casillas(models.Model):
    nombre = models.CharField(max_length=30)
    estacion=models.ForeignKey(estaciones,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class tipoVehiculo(models.Model):
    tipo=models.CharField(max_length=30,choices=tipo,default='' )
    precio=models.IntegerField()
    descripcion=models.CharField(max_length=100)
    def __str__(self) :
        return self.tipo

class ticket(models.Model):
    importe=models.IntegerField()
    fecha= models.DateField()
    hora=models.TimeField()
    tipoVehiculo=models.ForeignKey(tipoVehiculo,on_delete=models.CASCADE)
    def __str__(self) :
        return (f'{self.fecha} - {self.hora}') 

class turnos(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    dineroInicial= models.IntegerField()
    sentidoCirculacion=models.CharField(max_length=10,choices=sentido,default='este-oeste' )
    HoraPlanificadacomienzo=models.CharField(max_length=14,choices=horario,default='00:00 - 08:00' )
    casilla= models.ForeignKey(casillas,on_delete=models.CASCADE)
    def __str__(self):
        return self.fecha_creacion