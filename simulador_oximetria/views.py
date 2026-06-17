from gestion_esterilizadores.models import Esterilizador

from django.shortcuts import render



# Create your views here.

def simulador(request):
    if request.method=="POST":
        esterilizadores=Esterilizador.objects.get(id=1)
        esterilizadores.oximetria=esterilizadores.oximetria-1
        esterilizadores.save()
        return render(request,'simulador_oximetria/simulador.html',{'esterilizadores':esterilizadores})
    else:
        esterilizadores=Esterilizador.objects.get(id=1)
        return render(request,'simulador_oximetria/simulador.html',{'esterilizadores':esterilizadores})

