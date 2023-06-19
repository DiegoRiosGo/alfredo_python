from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from menu.models import Contacto, Raza
from .serializers import ContactoSerializers, RazaSerializers
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
def lista_raza(request):
    if request.method == 'GET':
       raza=Raza.objecs.all()
       serializer=RazaSerializers(Raza,many=True)
       return Response(serializer.data)

    elif request.method == 'POST':
       data = JSONParser().parse(request)
       serializer=RazaSerializers(data=data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['get','put','delete'])
def detalle_contacto(Request,id):
    
  try:
      Contacto=Contacto.objects.get(patente=id)
  except Contacto.DoesNotExist:
      return Response(status=status.http_404_not_found)

  if Request.method=='get':
      serializer=ContactoSerializers(Contacto)
      return Response(serializer.data)
  if Request.method=='put':
      data=JSONParser().parse(Request)
      serializer=ContactoSerializers(Contacto,data=data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      else:
          return Response(serializer.errors,status=status.http_400_bad_request)
  elif Request.method=='delete':
      Contacto.delete()
      return Response(status=status.http_204_no_content)
