from django.db import models

# Create your models here.
class Raza(models.Model):
    codigoRaza = models.AutoField(primary_key=True, verbose_name='Código de la Raza')
    nombreRaza = models.CharField(max_length=20,blank=False,null=True)

class Mascota(models.Model):
    codigoChip = models.CharField(primary_key=True)
    nombreMascota = models.CharField(max_length=50)
    edadMascota = models.IntegerField()
    foto = models.ImageField(upload_to="mascotas")
    raza = models.ForeignKey(Raza,on_delete=models.DO_NOTHING)