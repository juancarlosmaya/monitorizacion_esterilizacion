from django.shortcuts import render
from django.http import HttpResponse


def pagina_inicio(request):
    #return HttpResponse("<h1>Esta es la pagina de inicio</h1><h1>Hay dos opciones</h1> <p>Revisar usuarios</p> <p>Administrar usuarios</p> ")
    return render(request,'pagina_inicio.html')


#def acerca_de(request):
    #return HttpResponse("<h1>Aqui hay información de la empresa</h1>")
 #   return render(request,'acerca_de.html')


# Create your views here.



# ViewSets define the view behavior.
from gestion_esterilizadores.models import Esterilizador
from .serializers import serializadorEsterilizador
from rest_framework import viewsets

class vista_examinar_esterilizador(viewsets.ModelViewSet):
    queryset = Esterilizador.objects.all()
    serializer_class = serializadorEsterilizador
