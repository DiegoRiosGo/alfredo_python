from django.shortcuts import render
from django.db import models
from django.shortcuts import render, redirect
from .models import ReservaForm, NombreTabla_Contacto, NombreTabla_Registrarse,  NombreTabla_Login, NombreTabla_ContraseñaOlvidada,NombreTabla_ContraseñaOlvidada1

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
    Consulta = request.post("opt_Consulta"),
    Examen = request.post ("opt_Exame"),
    InterConsulta = request.post("opt_Inter"),
    Cirugias = request.post("opt_Cirugias"),
    Archivo = request.post("file"),
    Fecha_Reserva = request.post("arrive"),
    Mensaje = request.post("textarea2")

    ReservaForm.objects.create("nombre= Nombre", "email= Email", "tipo_reserva= Tipo_Reserva", "consulta = Consulta", "examen = Examen", "opt_inter = InterConsulta" , "opt_cirugia = Cirugias", "archivo = Archivo",
                               "fecha_reserva = Fecha_Reserva", "mensaje = Mensaje")
    

    return redirect('AgendaOnline')



def ingreso_contactos(request):
    Nombre_Contacto = request.post("nombre_contacto"),
    Correo = request.post("correo_contacto"),
    Numero = request.post("nro_contacto"),
    NombreMascota = request.post("nombre_m_contacto"),
    Mensaje_Contacto= request.post("msg_contacto")

    NombreTabla_Contacto.objects.create("nombre_contacto = Nombre_Contacto", "correo = Correo","numero_contacto = Numero","nombre_mascota = NombreMascota" ,
                                "mensaje_contacto = Mensaje_Contacto")
    
    return redirect('Contacto')

def ingreso_registrarse(request):
    Nombre_Completo = request.post("nombre"),
    Correo_Login = request.post ("correo"),
    Password = request.post ("contraseña"),
    Repetir_Contraseña = request.post("contraseña_nueva")

    NombreTabla_Registrarse.objects.create("nombre_completo = Nombre_Completo", "correo = Correo_Login","password = Password",
                                           "repetircontraseña = Repetir_Contraseña")
    
    return redirect('Login')


def inicioSesion(request):
    Correo_Login = request.post("correolog"),
    Contraseña_Login = request.post("contralog")

    NombreTabla_Login.objects.create("correologin = Correo_Login", "contraseñalogin = Contraseña_Login")

    return redirect('Inicio')


def olvidarContra(request):
    Correo_Olvida = request.post("correoOlvida0"),
    Contraseña_Olvida = request.post("contraseña0"),
    Contra_Nueva_Olvida = request.post("contranueva0")

    NombreTabla_ContraseñaOlvidada.objects.create("correo_olvidar = Correo_Olvida","nueva_contraseña = Contraseña_Olvida", "repetir_contraseña_nueva = Contra_Nueva_Olvida")

    return redirect('login')

def olvidarContra1(request):
    Correo_Olvida = request.post("correoOlvida"),
    Contraseña_Olvida = request.post("contraOlvida"),
    Contra_Nueva_Olvida = request.post("contraNueva")

    NombreTabla_ContraseñaOlvidada1.objects.create("correo_olvidar = Correo_Olvida","nueva_contraseña = Contraseña_Olvida", "repetir_contraseña_nueva = Contra_Nueva_Olvida")

    return redirect('login')