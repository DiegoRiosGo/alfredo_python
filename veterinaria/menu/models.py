from django.db import models

# Create your models here.
class Raza(models.Model):
    codigoRaza = models.AutoField(primary_key=True, verbose_name='Código de la Raza')
    nombreRaza = models.CharField(max_length=20,blank=False,null=True, verbose_name='Nombre de la mascota')

class Mascota(models.Model):
    codigoChip = models.CharField(primary_key=True)
    nombreMascota = models.CharField(max_length=50, verbose_name='Nombre de la mascota')
    edadMascota = models.IntegerField(verbose_name= 'Edad de la mascota')
    fechaNacimiento = models.DateField(auto_now=True, verbose_name= 'Fecha de nacimiento')
    foto = models.ImageField(upload_to="mascotas")
#falta agregar la fecha de nacimiento(listo)
    raza = models.ForeignKey(Raza,on_delete=models.DO_NOTHING)

class Servicios(models.Model):
    idServicio = models.AutoField(primary_key=True, verbose_name='Codigo de los servicios')
    nombreServicio = models.CharField(max_length=35, null=True, blank=False, verbose_name='Nombre de los servicios')
    precioServicio = models.IntegerField(max_length=6, null=True, blank=False, verbose_name='El precio de los servicios ')

class especialidad(models.Model):
    idEspecialidad = models.AutoField(primary_key= True, verbose_name= 'Codigo de la especialidad')
    nombreEspecialidad = models.CharField(max_length=35, null=True, blank=False, verbose_name='Nombre de la especialidad')

class region(models.Model):
    idRegion = models.IntegerField(primary_key=True, verbose_name='Codigo de la region')
    nombreRegion = models.CharField(max_length=35, null=True, blank=False, verbose_name='Nombre de la region')

class comuna(models.Model):
    idComuna = models.IntegerField(primary_key=True, verbose_name= 'Codigo de la comuna')
    region = models.ForeignKey(region, on_delete=models.DO_NOTHING)

class rol(models.Model):
    idRol = models.IntegerField(primary_key=True, null=True, blank=False, verbose_name='Codigo del rol de usuario')
    nombreRol = models.CharField(max_length=45, null=True, blank=False, verbose_name='Nombre del rol de usuario')

class preguntas(models.Model):
    idPreguntas = models.IntegerField(primary_key=True, max_length=50, null=True, blank=False, verbose_name='Mensaje de consulta')
    nombrePregunta = models.CharField(max_length=35, null=True, blank=False, verbose_name= 'Nombre de la persona que hace las preguntas')









