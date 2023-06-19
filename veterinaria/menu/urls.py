from django.contrib import admin
from django.urls import path, include
from .views import Inicio,InicioLogueado,Nosotros,AgendaOnline,Contacto,Login,OlvidoContra,Servicios, crear_reserva, ingreso_contactos, ingreso_registrarse, inicioSesion,eliminarR,eliminarC, modificarcontraseña,paginalogin


urlpatterns = [
    path('Inicio/',Inicio,name="Inicio"),
    path('InicioLogueado/',InicioLogueado,name="InicioLogueado"),
    path('Nosotros/',Nosotros,name="Nosotros"),
    path('AgendaOnline/',AgendaOnline,name="AgendaOnline"),
    path('Contacto/',Contacto,name="Contacto"),
    path('Login/',Login,name="Login"),
    path('OlvidoContra/',OlvidoContra,name="OlvidoContra"),
    path('Servicios/', Servicios,name="Servicios"),
    #--fin html
    path('crear_reserva/', crear_reserva, name="crear_reserva"),
    path('eliminarR/<id>', eliminarR, name="eliminarR"),
    path('ingreso_contactos/',ingreso_contactos, name="ingreso_contactos"),
    path('eliminarC/<id>', eliminarC, name="eliminarC"),
    path('ingreso_registrarse/',ingreso_registrarse, name="ingreso_registrarse"),

    path('inicioSesion/', inicioSesion, name="login"),
    
    path('modificarcontraseña/', modificarcontraseña, name="modificarcontraseña"),
     path('paginalogin/', paginalogin, name="paginalogin"),


    '''
    path('modificar/<id>',modificar, name="modificar"),
    path('paginalogin/',paginalogin, name="paginalogin"),
    path('eliminar/ <id>', eliminar, name="eliminar"),
    path('Historial_Medico1DatosM/', Historial_Medico1DatosM, name="Historial_Medico1DatosM"),
    path('Historial_Medico2DatosD/', Historial_Medico2DatosD, name="Historial_Medico2DatosD"),
    path('registroMascota/', registroMascota, name="registroMascota"),
    '''
    #---------------------------------vistas de formularios

]