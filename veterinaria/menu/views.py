from django.shortcuts import render

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