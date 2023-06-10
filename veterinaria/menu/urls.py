from django.contrib import admin
from django.urls import path, include
from .views import Inicio,Nosotros,AgendaOnline,Contacto,Login,OlvidoContra,Servicios

urlpatterns = [
    path('',Inicio,name="Inicio"),
    path('Nosotros/',Nosotros,name="Nosotros"),
    path('AgendaOnline/',AgendaOnline,name="AgendaOnline"),
    path('Contacto/',Contacto,name="Contacto"),
    path('Login/',Login,name="Login"),
    path('OlvidoContra/',OlvidoContra,name="OlvidoContra"),
    path('Servicios/',Servicios,name="Servicios"),
    #---------------------------------vistas de formularios
    path('crear_reserva/',crear_reserva,name="crear_reserva"),
    path('ingreso_contactos/',ingreso_contactos,name="ingreso_contactos"),
    path('ingreso_registrarse/',ingreso_registrarse,name="ingreso_registrarse"),
]