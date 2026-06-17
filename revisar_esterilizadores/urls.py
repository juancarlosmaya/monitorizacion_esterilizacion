from django.urls import path
from .views import revisar_esterilizadores

urlpatterns = [
    path('',revisar_esterilizadores),
    
]
