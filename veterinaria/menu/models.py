from django.db import models
#Import Model Agregado
from django.db.models import Model

# Create your models here.
class Raza(models.Model):
    codigoRaza = models.AutoField(primary_key=True, verbose_name='Código de la Raza')
    nombreRaza = models.CharField(max_length=20,blank=False,null=True, verbose_name='Nombre de la mascota')

    def __str__(self) -> str:
        return self.nombreRaza

class Servicios(models.Model):
    idServicio = models.AutoField(primary_key=True, verbose_name='Codigo de los servicios')
    nombreServicio = models.CharField(max_length=35, null=True, blank=False, verbose_name='Nombre de los servicios')
    precioServicio = models.IntegerField( null=True, blank=False, verbose_name='El precio de los servicios ')

    def __str__(self) -> str:
        return self.nombreServicio

#---vistas---
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name='Codigo de usuario')
    nombrecompletoUsuario = models.CharField(max_length=50,  null=True, blank=False, verbose_name='Nombre del usuario')
    correoUsuario = models.EmailField(max_length= 45, null=True, blank=False,verbose_name='Correo del usuario')
    claveUsuario = models.CharField(max_length=20, null=True, blank=False, verbose_name='Contraseña del usuario')

    def __str__(self) -> str:
        return self.correoUsuario
        
#nose si funciona
class Mascota(models.Model):
    codigoChip = models.IntegerField(primary_key=True, verbose_name='Codigo chip mascota')
    MascotaNombre = models.CharField(max_length=50, null=True, blank=False, verbose_name='Nombre de la mascota')
    edadMascota = models.IntegerField(null=True, blank=False, verbose_name= 'Edad de la mascota')
    fechaNacimiento = models.DateField(auto_now=True, verbose_name= 'Fecha de nacimiento')
    enfermedades = models.CharField(max_length=30,null=True, blank=False, verbose_name='Enfermedad de la mascota' )
    foto = models.ImageField(upload_to="mascotas")
    raza = models.ForeignKey(Raza,on_delete=models.DO_NOTHING)
    nombreDueno = models.CharField(max_length=50, null=True, blank=False, verbose_name='Nombre del dueno')

    def __str__(self) -> str:
        return self.MascotaNombre

#tabla funcional correcta
class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True,  verbose_name='Codigo de reserva')
    nombreUsuario = models.CharField( max_length=30,null=True, blank=False, verbose_name='Nombre del usuario' )
    correoUsuario = models.EmailField(max_length=50, null=True, blank=False, verbose_name='Correo del usuario')
    tipoReserva = models.ForeignKey(Servicios,on_delete=models.DO_NOTHING,verbose_name='Tipo de reserva')
    nombreMascota = models.CharField(max_length=20, null=True, blank=False, verbose_name='nombre de la mascota')
    edadMascota = models.CharField(max_length=20, null=True, blank=False, verbose_name='Edad de la mascota')
    Archivos = models.ImageField(upload_to='Reserva', verbose_name='Archivos')
    fechaReserva = models.DateField(auto_now=True, verbose_name='Fecha de la reservacion')
    mensajeReserva = models.CharField(max_length=50, verbose_name='Mensaje de las reservaciones')
    

#tabla funcional correcta
class Contacto(models.Model):
    idContacto = models.AutoField(primary_key=True, verbose_name='Codigo de contact')
    NombreContacto = models.CharField( max_length=30, null=True, blank=False,verbose_name='Nombre del contacto')
    correoContacto = models.EmailField(max_length=30, null=True, blank=False, verbose_name='Correo del contacto')
    TelefonoContacto = models.IntegerField(null=True, blank=False, verbose_name='Telefono de contacto')
    nombreMascota = models.CharField(max_length=30, null=True, blank=False,verbose_name='Nombre de la mascota')
    mensajeContacto = models.CharField(max_length=50, null=True, blank=False, verbose_name='Mensaje del contacto')

class Respuesta(models.Model):
    idRespuestas = models.AutoField(primary_key=True, verbose_name='Id Repsuesta')
    contenidoRespuesta = models.CharField(max_length=50, null=True, blank=False, verbose_name='Contendio de la respuesta')