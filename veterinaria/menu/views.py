from django.shortcuts import render, redirect,get_object_or_404
from django.db import models
from django.shortcuts import render, redirect
from .models import Raza,Servicios,Usuario,Mascota,Reserva,Contacto,Respuesta
from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.
# vista clientes
def Inicio(request):
    return render(request,'menu/HTML/Inicio.html')

def InicioLogueado(request):
    return render(request,'menu/HTML/InicioLogueado.html')

def Nosotros(request):
    return render(request,'menu/HTML/Nosotros.html')

def AgendaOnline(request):
    datos = Servicios.objects.all()
    contexto = {
        "servicios":datos
    }
    return render(request,'menu/HTML/AgendaOnline.html',contexto)

def Contactos(request):
    return render(request,'menu/HTML/Contacto.html')

def Login(request):
    return render(request,'menu/HTML/Login.html')

def OlvidoContra(request):
    return render(request,'menu/HTML/OlvidoContra.html')

def Servicios(request):
    return render(request,'menu/HTML/Servicios.html')

#vistas administradores 
def Contacto_Clientes(request):
    listaC = Contacto.objects.all()
    contexto={
        "contactos": listaC
    }
    return render(request,'menu/ADMINISTRADOR/Contacto_Cliente.html',contexto)

def Historial_Medico(request):
    listaMascota = Mascota.objects.all()
    contexto={
        "mascotas": listaMascota
    }
    return render(request,'menu/ADMINISTRADOR/Historial_Medico.html',contexto)

def Inicio_adm(request):
    return render(request,'menu/ADMINISTRADOR/Inicio_adm.html')

def Registro_paciente(request):
    datos = Raza.objects.all()
    contexto = {
        "razas":datos
    }
    return render(request,'menu/ADMINISTRADOR/Registro_paciente.html',contexto)    

def RevisarCitas(request):
    listaR = Reserva.objects.all()
    contexto={
        "reservas": listaR
    }
    return render(request,'menu/ADMINISTRADOR/RevisarCitas.html',contexto)


#---fin html

#funcional  1
def crear_reserva(request):
    Nombre = request.post['username'],
    Email = request.post['email'],
    Tipo_Reserva = request.post['tipo'],
    mascotaM = request.post['Nombre_Mas'],
    mascotaE = request.post['edad_mas'],
    Archivo = request.FILES['archivoS'],
    Fecha_Reserva = request.post['reservaF'],
    Mensaje = request.post['mensajeC'],

    registroServicio = Servicios.objects.get(idServicio = Tipo_Reserva)
    Reserva.objects.create(nombreUsuario= Nombre, correoUsuario= Email, tipoReserva= registroServicio, nombreMascota=mascotaM,
                            edadMascota= mascotaE,Archivos = Archivo,fechaReserva = Fecha_Reserva, mensajeReserva = Mensaje)
    
    return redirect('AgendaOnline')

#eliminar reserva funcional
def eliminarR(request,id):
    reserva=Reserva.objects.get(idReserva=id)
    reserva.delete()

    return redirect('RevisarCitas')

#funcional
def ingreso_contactos(request):
    Nombre_Contacto = request.POST['nombre_contacto']
    Correo = request.POST['correo_contacto']
    Numero = request.POST['nro_contacto']
    NombreMascota = request.POST['nombre_m_contacto']
    Mensaje_Contacto= request.POST['msg_contacto']

    Contacto.objects.create (NombreContacto = Nombre_Contacto, correoContacto = Correo,TelefonoContacto = Numero,nombreMascota = NombreMascota ,
                                mensajeContacto = Mensaje_Contacto)
    
    return redirect('Contactos')

def eliminarC(request,id):
    contactos=Contacto.objects.get(idContacto=id)
    contactos.delete()

    return redirect('Contacto_Clientes')

#respuesta del contacto
def Respuestas(request):
    respuesta = request.post['contRespuesta']

    Respuesta.objects.create(contenidoRespuesta = respuesta)

    #crear html con respuesta 
    return redirect('Respuestas')

def ingreso_mascota(request):
    codigoM = request.post['Codigo']
    nombreM = request.post['nombre_mascota'],
    edadM = request.post['Edad'],
    fechaM = request.post['Fecha'],
    enfermedadM = request.post['enfermedades'],
    archivoM= request.FILES['archivo_mascota']
    razaM= request.post['raza']
    nombreD= request.post['dueno']

    registroRaza = Raza.objects.get(codigoRaza = razaM)
    Mascota.objects.create(codigoChip = codigoM, MascotaNombre = nombreM, edadMascota = edadM, fechaNacimiento = fechaM ,
                                enfermedades = enfermedadM, foto = archivoM, raza = registroRaza, nombreDueno = nombreD)
    
    return redirect('Contacto')

def eliminarM(request,id):
    mascota=Mascota.objects.get(codigoChip=id)
    mascota.delete()

    return redirect('Historial_Medico')


def ingreso_registrarse(request):
    Nombre_Completo = request.POST['nombre']
    Correo_Login = request.POST ['correo']
    Password = request.POST ['contraseña']

    Usuario.objects.create(nombrecompletoUsuario = Nombre_Completo, correoUsuario = Correo_Login , claveUsuario = Password)
    
    return redirect('Inicio')


#para mas rato
def inicioSesion(request,id):
    inicio=Usuario.objects.get(idUsuario=id)

    contexto = {
        'datos':inicio
    }
    return render('Inicio',contexto)



@login_required

def modificarcontraseña(request,id):

    correo = request.POST['correoUsuario']
    contra = request.POST['claveUsuario']

    r_original = Usuario.objects.get(idUsuario= id) #el registro original
    #comienzo a reemplazar los valores en ese registro original
    r_original.correoUsuario = correo
    r_original.correoUsuario = contra

    r_original.save() #update
    return redirect('Login')





def paginalogin (request):
    if request.method=='POST':
        try:
            datosUsuario=Usuario.objects.get(correoUsuario=request.POST['correolog'],claveUsuario=request.POST['contralog'])
            print("Usuario=",datosUsuario)
            if(datosUsuario.correoUsuario=="admin@vetjuanita.cl"):
                return redirect('Inicio_adm')
            else:
                return redirect('InicioLogueado')
        except Usuario.DoesNotExist as e:
            messages.success(request,'¡Correo o Contraseña no correcto!')

    return render(request, 'Login')
