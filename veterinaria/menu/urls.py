from django.contrib import admin
from django.urls import path, include
from .views import Inicio,Nosotros

urlpatterns = [
    path('',Inicio,name="Inicio"),
    path('Nosotros/',Nosotros,name="Nosotros"),
    #----------
    path('paginaNosotros/',Nosotros,name="Nosotros"),
]