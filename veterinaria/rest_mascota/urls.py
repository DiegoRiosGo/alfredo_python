from rest_mascota.views import views, lista_contacto, detalle_contacto
from django.urls import path

urlpatterns = [
    path('lista_contacto',lista_contacto, name='lista_contacto'),
    path('detalle_contacto',detalle_contacto, name='detalle_contacto')
]






