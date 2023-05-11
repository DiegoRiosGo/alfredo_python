from django.contrib import admin
from django.urls import path, include
from .views import Inicio,Nosotros,AgendaOnline,Contacto,Login,OlvidoContra,Servicios

urlpatterns = [
    path('',Inicio,name="Inicio"),
    path('Nosotros/',Nosotros,name="Nosotros"),
    #----------
    path('AgendaOnline/',AgendaOnline,name="AgendaOnline"),
    path('Contacto/',Contacto,name="Contacto"),
    path('Login/',Login,name="Login"),
    path('OlvidoContra/',OlvidoContra,name="OlvidoContra"),
    path('Servicios/',Servicios,name="Servicios"),
]