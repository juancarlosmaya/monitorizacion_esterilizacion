from django.urls import path
from .views import simulador


urlpatterns = [
   
    # páginas de incio
    path('',simulador,name='simulador'), 
    

]