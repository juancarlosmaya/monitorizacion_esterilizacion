# Serializers define the API representation.
from gestion_usuarios.models import usuario
from rest_framework import serializers
class serializadorUsuario(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ['nombre', 'cedula', 'fecha_nacimiento', 'frecha_registro','conectado','oximetria','frecuenciaCardiaca','pletismografia','valoresValidos','numeroPicos','balanceIRRDC','fiO2','pip','vt','frecuenciaRespitatoria','presion','volumen','flujo']

