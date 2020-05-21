from gestion_usuarios.models import usuario
import time
from django.shortcuts import render
from django.http import HttpResponse


miVariable=0
def revisar_usuarios(request):
    global miVariable
    
    usuarios=usuario.objects.all()  # lee todos los usuarios en la base de datos

    if request.method=="POST":
        nombre_seleccionado=request.POST.get("nombre_seleccionado")
        usuario_seleccionado = usuario.objects.get(nombre=nombre_seleccionado)
        print(usuario_seleccionado.nombre)
        time.sleep(1)
        miVariable=miVariable+1
        return render(request,'revisar_usuarios/revisar_usuario.html',{'usuarios':usuarios,'usuario_seleccionado':usuario_seleccionado,'miVariable':miVariable})
    #return HttpResponse("<h1>Esta es la pagina de inicio</h1><h1>Hay dos opciones</h1> <p>Revisar usuarios</p> <p>Administrar usuarios</p> ")
    return render(request,'revisar_usuarios/revisar_usuario.html',{'usuarios':usuarios})




