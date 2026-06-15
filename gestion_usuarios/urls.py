from django.urls import path
from .views import solicitar_nombre
from .views import gracias

urlpatterns = [
    path('',solicitar_nombre,name='gestion'),
    path('gracias',gracias),
   
    
]
