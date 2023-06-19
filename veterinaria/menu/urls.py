from django.contrib import admin
from django.urls import path, include
from .views import Inicio,InicioLogueado,Nosotros,AgendaOnline,Contactos,Login,OlvidoContra,Servicio, crear_reserva, ingreso_contactos, ingreso_registrarse, inicioSesion,eliminarR,eliminarC, modificarcontraseña,paginalogin


urlpatterns = [
    path('',Inicio,name="Inicio"),
    path('InicioLogueado/',InicioLogueado,name="InicioLogueado"),
    path('Nosotros/',Nosotros,name="Nosotros"),
    path('AgendaOnline/',AgendaOnline,name="AgendaOnline"),
    path('Contactos/', Contactos ,name="Contactos"),
    path('Login/',Login,name="Login"),
    path('OlvidoContra/',OlvidoContra,name="OlvidoContra"),
    path('Servicio/', Servicio,name="Servicio"),
    #--fin html
    path('crear_reserva/', crear_reserva, name="crear_reserva"),
    path('eliminarR/<id>', eliminarR, name="eliminarR"),
    path('ingreso_contactos/',ingreso_contactos, name="ingreso_contactos"),
    path('eliminarC/<id>', eliminarC, name="eliminarC"),
    path('ingreso_registrarse/',ingreso_registrarse, name="ingreso_registrarse"),

    path('inicioSesion/', inicioSesion, name="login"),
    
    path('modificarcontraseña/', modificarcontraseña, name="modificarcontraseña"),
     path('paginalogin/', paginalogin, name="paginalogin"),



    #---------------------------------vistas de formularios

]