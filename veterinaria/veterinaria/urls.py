"""veterinaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import crear_reserva, contactos, registrarse, inicioSesion,olvidarContra,olvidarContra1,modificar,eliminar,paginalogin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('menu.urls')),
    path('crear_reserva/', crear_reserva, name="crear_reserva"),
    path('contactos/',contactos, name="contactos"),
    path('registrarse/',registrarse, name="Registrarse"),
    path('inicioSesion/', inicioSesion, name="login"),
    path('olvidarContra/',olvidarContra, name="OlvidoContra"),
    path('olvidarContra1/',olvidarContra1, name="olvidaste contraseña"),
    path('modificar/',modificar, name="modificar"),
    path('paginalogin/',paginalogin, name="paginalogin"),
    path('eliminar/',paginalogin, name="paginalogin")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


    