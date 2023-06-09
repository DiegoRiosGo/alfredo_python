from django.contrib import admin
from django.urls import path, include
from .views import Inicio,Nosotros,AgendaOnline,Contacto,Login,OlvidoContra,Servicios,crear_reserva,contactos,registrarse,inicioSesion

urlpatterns = [
    path('',Inicio,name="Inicio"),
    path('Nosotros/',Nosotros,name="Nosotros"),
    #----------
    path('AgendaOnline/',AgendaOnline,name="AgendaOnline"),
    path('Contacto/',Contacto,name="Contacto"),
    path('Login/',Login,name="Login"),
    path('OlvidoContra/',OlvidoContra,name="OlvidoContra"),
    path('Servicios/',Servicios,name="Servicios"),
    path('crear_reserva/',crear_reserva,name="crear_reserva"),
    path('contactos/',contactos,name="contactos"),
    path('registrarse/',registrarse,name="registrarse"),
    path('inicioSesion/',inicioSesion,name="inicioSesion"),
]