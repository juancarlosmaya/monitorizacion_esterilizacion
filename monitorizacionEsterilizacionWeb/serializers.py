# Serializers define the API representation.
from gestion_esterilizadores.models import Esterilizador
from rest_framework import serializers
class serializadorEsterilizador(serializers.ModelSerializer):
    class Meta:
        model = Esterilizador
        fields = ['tipo', 'modelo', 'serie', 'volumen', 'registro_sanitario','conectado','temperatura_actual','temperatura','presion_actual','presion']

