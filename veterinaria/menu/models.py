from django.db import models

# Create your models here.
class Raza(models.Model):
    codigoRaza = models.AutoField(primary_key=True, verbose_name='Código de la Raza')
    nombreRaza = models.CharField(max_length=20,blank=False,null=True, verbose_name='Nombre de la mascota')

class Mascota(models.Model):
    codigoChip = models.CharField(primary_key=True)
    nombreMascota = models.CharField(max_length=50, verbose_name='Nombre de la mascota')
    edadMascota = models.IntegerField()
    foto = models.ImageField(upload_to="mascotas")
#falta agregar la fecha de nacimiento
    raza = models.ForeignKey(Raza,on_delete=models.DO_NOTHING)

class Servicios(models.Model):
    idServicio = models.AutoField(primary_key=True, verbose_name='Codigo de los servicios')
    nombreServicio = models.CharField(max_length=35, blank=False, null=True, verbose_name='Nombre de los servicios')
    precioServicio = models.

class