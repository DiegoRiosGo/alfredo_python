from rest_framework import serializers
from core.models import Raza,Servicios,Usuario,Mascota,Reserva,Contacto,Respuesta

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['idContacto','NombreContacto','correoContacto','TelefonoContacto','nombreMascota','mensajeContacto']

class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = ['codigoRaza','nombreRaza']



