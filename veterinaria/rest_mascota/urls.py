from rest_mascota.views import lista_raza, detalle_contacto
from django.urls import path

urlpatterns = [
    path('lista_raza',lista_raza, name='lista_raza'),
    path('detalle_contacto',detalle_contacto, name='detalle_contacto')
]






