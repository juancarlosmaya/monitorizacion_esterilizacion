from gestion_esterilizadores.models import Esterilizador
import time
from django.shortcuts import render
from django.http import HttpResponse


miVariable=0
def revisar_esterilizadores(request):
    global miVariable
    
    esterilizadores=Esterilizador.objects.all()  # lee todos los esterilizadores en la base de datos

    if request.method=="POST":
        modelo_seleccionado=request.POST.get("nombre_seleccionado")
        print("MODELO SELECCIONADO:")
        print(modelo_seleccionado)
        esterilizador_seleccionado = Esterilizador.objects.get(modelo=modelo_seleccionado)
        print(esterilizador_seleccionado.temperatura)
        time.sleep(1)
        miVariable=miVariable+1
        return render(request,'revisar_esterilizadores/revisar_esterilizador.html',{'esterilizadores':esterilizadores,'esterilizador_seleccionado':esterilizador_seleccionado,'miVariable':miVariable})
    #return HttpResponse("<h1>Esta es la pagina de inicio</h1><h1>Hay dos opciones</h1> <p>Revisar usuarios</p> <p>Administrar usuarios</p> ")
    return render(request,'revisar_esterilizadores/revisar_esterilizador.html',{'esterilizadores':esterilizadores})




