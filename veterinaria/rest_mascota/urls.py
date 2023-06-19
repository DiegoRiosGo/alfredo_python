from django.contrib import admin
from django.urls import path
from rest_mascota.views import lista_contacto, detalle_contacto

urlpatterns = [
    path('lista_contacto',lista_contacto, name='lista_contacto'),
    path('detalle_contacto',detalle_contacto, name='detalle_contacto')
]






