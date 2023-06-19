from rest_mascota.views import views
from django.urls import path

urlpatterns = [
    path('lista_contacto',views.lista_contacto, name='lista_contacto'),
    path('detalle_contacto',views.detalle_contacto, name='detalle_contacto')
]






