from secrets import choice
from statistics import mode
from tkinter import CASCADE
from django.db import models
from .tipoDocumento import documento
from .sentido import sentido
from .tipoVehiculo import tipo
from .horarios import horario
from django.utils import timezone
from django.conf import settings

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
    usuario =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
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
        return (f'{self.nombre} {self.estacion.nombre}') 

class tipoVehiculo(models.Model):
    tipo=models.CharField(max_length=30,choices=tipo,default='' )
    precio=models.IntegerField()
    descripcion=models.CharField(max_length=100)
    def __str__(self) :
        return self.tipo

class turnos(models.Model):
    fecha_creacion = models.DateTimeField(null=True,blank=True)
    fecha_fin=models.DateTimeField(null=True,blank=True)
    dineroInicial= models.IntegerField()
    sentidoCirculacion=models.CharField(max_length=10,choices=sentido,default='este-oeste' )
    HoraPlanificada=models.CharField(max_length=14,choices=horario,default='00:00 - 08:00' )
    turno_activo = models.BooleanField(default=True)
    casilla= models.ForeignKey(casillas,on_delete=models.CASCADE)
    operador= models.ForeignKey(operadores,on_delete=models.CASCADE, null=True,blank=True)
    
    def __str__(self):
        return (f'{self.sentidoCirculacion}, {self.HoraPlanificada}, {self.turno_activo}') 


class ticket(models.Model):
    importe=models.IntegerField()
    fecha= models.DateField()
    hora=models.TimeField()
    tipoVehiculo=models.ForeignKey(tipoVehiculo,on_delete=models.CASCADE)
    turno= models.ForeignKey(turnos,on_delete=models.CASCADE)
    def __str__(self) :
        return (f'{self.fecha}, {self.hora}, {self.tipoVehiculo}, {self.importe}, {self.turno}') 


class quejas(models.Model):
    nombreCompleto = models.CharField(max_length=20)
    gmail = models.EmailField()
    tituloQueja = models.CharField(max_length=25)
    contenidoQueja = models.TextField(max_length=300)
    fechaReclamo = models.DateTimeField(null=True)  
    ticket = models.ForeignKey(ticket, on_delete=models.CASCADE)
    