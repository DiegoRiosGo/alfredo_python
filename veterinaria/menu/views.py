from django.shortcuts import render
from django.db import models
from django.shortcuts import render, redirect
from .models import Reserva,Raza,Region,Registarse,Respuesta,Rol,Especialidad,Usuario,iniciosesion,Preguntas,Servicios,Detalle,Comuna,Consulta,Contacto,Mascota,Mensaje,Model

# Create your views here.
def Inicio(request):
    return render(request,'menu/HTML/Inicio.html')

def Nosotros(request):
    return render(request,'menu/HTML/Nosotros.html')
#-----------------
def AgendaOnline(request):
    return render(request,'menu/HTML/AgendaOnline.html')

def Contacto(request):
    return render(request,'menu/HTML/Contacto.html')

def Login(request):
    return render(request,'menu/HTML/Login.html')

def OlvidoContra(request):
    return render(request,'menu/HTML/OlvidoContra.html')

def Servicios(request):
    return render(request,'menu/HTML/Servicios.html')
    




def crear_reserva(request):
    Nombre = request.post("username"),
    Email = request.post("email"),
    Tipo_Reserva = request.post("tipo"),
    Chip = request.post("Id_Chip")
    Archivo = request.post("file"),
    Fecha_Reserva = request.post("arrive"),
    Mensaje = request.post("textarea2")

    Reserva.objects.create("nombreUsuario= Nombre", "correoUsuarios= Email", "tipoReserva= Tipo_Reserva","chip = Chip", "Archivos = Archivo",
                               "fechaReserva = Fecha_Reserva", "mensajeReserva = Mensaje")
    

    return redirect('AgendaOnline')



def contactos(request):
    Nombre_Contacto = request.post("nombre_contacto"),
    Correo = request.post("correo_contacto"),
    Numero = request.post("nro_contacto"),
    NombreMascota = request.post("nombre_m_contacto"),
    Mensaje_Contacto= request.post("msg_contacto")

    Contacto.objects.create("NombreContacto = Nombre_Contacto", "correoContacto = Correo","TelefonoContacto = Numero","nombreMascota = NombreMascota" ,
                                "mensajeContacto = Mensaje_Contacto")
    
    return redirect('Contacto')

def registrarse(request):
    Nombre_Completo = request.post("nombre"),
    Correo_Login = request.post ("correo"),
    Password = request.post ("contraseña"),
    Repetir_Contraseña = request.post("contraseña_nueva")

    Registarse.objects.create("nombrecompletoUsuario = Nombre_Completo", "correoUsuario = Correo_Login","claveRegistrarse = Password",
                                           "ClavenuevaRegistrarse = Repetir_Contraseña")
    
    return redirect('Login')

#____________________________________________


def inicioSesion (request):
    Correo_Login = request.post("correolog"),
    Contraseña_Login = request.post("contralog")

    iniciosesion.objects.create("correo = Correo_Login", "claveUsuario = Contraseña_Login")

    return redirect('Inicio')
