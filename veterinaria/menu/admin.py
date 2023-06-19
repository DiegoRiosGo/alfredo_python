from django.contrib import admin
from .models import Raza,Servicios,Usuario,Mascota,Reserva,Contacto,Respuesta
# Register your models here.

admin.site.register(Raza)
admin.site.register(Servicios)

admin.site.register(Usuario)
admin.site.register(Mascota)
admin.site.register(Respuesta)
admin.site.register(Contacto)
admin.site.register(Reserva)

