from rest_framework import serializers
from gestion_esterilizadores.models import esterilizador

class Esterilizador_Serializador(serializers.ModelSerializer):
    class Meta:
        model= esterilizador
        fields=('id','tipo','modelo','serie','volumen','registro_sanitario','conectado','temperatura_actual','temperatura','presion_actual','presion')
