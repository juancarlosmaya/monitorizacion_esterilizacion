from django.urls import path
from .views import revisar_usuarios

urlpatterns = [
    path('',revisar_usuarios),
    
]
