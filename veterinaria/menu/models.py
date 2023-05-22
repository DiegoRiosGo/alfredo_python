from django.db import models
#Import Model Agregado
from django.db.models import Model

# Create your models here.
class Raza(models.Model):
    codigoRaza = models.AutoField(primary_key=True, verbose_name='Código de la Raza')
    nombreRaza = models.CharField(max_length=20,blank=False,null=True, verbose_name='Nombre de la mascota')

class Servicios(models.Model):
    idServicio = models.AutoField(primary_key=True, verbose_name='Codigo de los servicios')
    nombreServicio = models.CharField(max_length=35, null=True, blank=False, verbose_name='Nombre de los servicios')
    precioServicio = models.IntegerField( null=True, blank=False, verbose_name='El precio de los servicios ')

class Especialidad(models.Model):
    idEspecialidad = models.AutoField(primary_key= True, verbose_name= 'Codigo de la especialidad')
    nombreEspecialidad = models.CharField(max_length=35, null=True, blank=False, verbose_name='Nombre de la especialidad')

class Region(models.Model):
    idRegion = models.IntegerField(primary_key=True, verbose_name='Codigo de la region')
    nombreRegion = models.CharField(max_length=35, null=True, blank=False, verbose_name='Nombre de la region')

class Comuna(models.Model):
    idComuna = models.IntegerField(primary_key=True, verbose_name= 'Codigo de la comuna')
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING)

class Rol(models.Model):
    idRol = models.IntegerField(primary_key=True, null=True, blank=False, verbose_name='Codigo del rol de usuario')
    nombreRol = models.CharField(max_length=45, null=True, blank=False, verbose_name='Nombre del rol de usuario')

class Preguntas(models.Model):
    idPreguntas = models.IntegerField(primary_key=True, null=True, blank=False, verbose_name='Mensaje de consulta')
    nombrePregunta = models.CharField(max_length=35, null=True, blank=False, verbose_name= 'Nombre de la persona que hace las preguntas')

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, blank=False, null=True, verbose_name='Codigo de usuario')
    rutUsuario = models.CharField(max_length=10, blank=False, null=True, verbose_name='Rut del usuario')
    primerNombreUsuario = models.CharField(max_length=30, verbose_name='Nombre del usuario')
    apellidoUsuario = models.CharField(max_length=30, verbose_name='Apellido del usuario')
    correoUsuario = models.EmailField(max_length= 45,verbose_name='Correo del usuario')
    direccionUsuario = models.CharField(max_length= 50, verbose_name='Direccion del usuario')
    fechanacUsuario = models.DateField(auto_now=True, verbose_name='Fecha de nacimiento del usuario')
    idComuna = models.ForeignKey(Comuna, on_delete=models.DO_NOTHING)
    idRol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING)
    idEspecialidad = models.ForeignKey(Especialidad, on_delete=models.DO_NOTHING)
    nombreUsuario = models.CharField(max_length=20, null=True, blank=False, verbose_name='Nombre de inicio sesion del usuario')
    claveUsuario = models.CharField(max_length=20, null=True, blank=False, verbose_name='Conrtaseña del usuario')
    idPreguntas = models.ForeignKey(Preguntas, on_delete=models.DO_NOTHING, verbose_name='Codigo de la pregunta')
    respuestaUsuario = models.CharField(max_length=50, null=True, blank=False, verbose_name='Respuesta al mensaje')
    telefonoUsuario = models.IntegerField(null=True, blank=False, verbose_name='Telefono del usuario')

class Mascota(models.Model):
    codigoChip = models.IntegerField(primary_key=True)
    nombreMascota = models.CharField(max_length=50, verbose_name='Nombre de la mascota')
    edadMascota = models.IntegerField(verbose_name= 'Edad de la mascota')
    fechaNacimiento = models.DateField(auto_now=True, verbose_name= 'Fecha de nacimiento')
    foto = models.ImageField(upload_to="mascotas")
#falta agregar la fecha de nacimiento(listo)
    raza = models.ForeignKey(Raza,on_delete=models.DO_NOTHING)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

class Consulta(models.Model):
    idConsulta = models.AutoField(primary_key=True, null=True, blank=False, verbose_name='Codigo de la consulta')
    idMascota = models.ForeignKey(Mascota, on_delete=models.DO_NOTHING)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

class Detalle(models.Model):
    idDetalle = models.AutoField(primary_key=True, null=True, blank=False, verbose_name='Codigo del detalle')

class Mensaje(models.Model):
    idMensaje = models.AutoField(primary_key=True, null=True, blank=False, verbose_name='Codigo del mensaje')
    asuntoMensaje = models.CharField(max_length=10, null=True, blank=False, verbose_name='Asunto del mensaje')
    descripcionMensaje = models.CharField(max_length=10, null=True, blank=False, verbose_name='Descripcion del mensaje')
    idUsuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    fechaenvioMensaje = models.DateField(auto_now=True, verbose_name='Fecha de envio de los mensajes')
    fechalecturaMensaje = models.DateField(auto_now=True, verbose_name='Fecha de la lectura de los mensajes')
    statusMensaje = models.CharField(max_length=10, null=True, blank=False, verbose_name='Status del mensaje')
#statusMensaje, falta agregar

class Respuesta(models.Model):
    idRespuesta = models.AutoField(primary_key=True, null=True, blank=False, verbose_name='Codigo de la respuesta')
    descripcionRespuesta = models.CharField(max_length=50, null=True, blank=False, verbose_name='Descripcion de la respuesta de los mensajes')
    idMensaje = models.ForeignKey(Mensaje, on_delete=models.DO_NOTHING)
    statusRespuesta = models.CharField(max_length=10, null=True, blank=False, verbose_name='Status de la respuesta de los mensajes')




    











