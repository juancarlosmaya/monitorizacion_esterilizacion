
from django.db import models

# Create your models here.

class Esterilizador(models.Model):
    tipo                    = models.CharField(max_length=20)
    modelo                  = models.CharField(max_length=20)
    serie                   = models.CharField(max_length=20)
    volumen                 = models.CharField(max_length=20)
    registro_sanitario      = models.CharField(max_length=20)

    conectado               = models.BooleanField()    

    # TEMPERATURA
    temperatura_actual      = models.DecimalField(decimal_places=0,max_digits=3)
    #frecuenciaCardiaca     = models.DecimalField(decimal_places=0,max_digits=3)
    temperatura              = models.JSONField()
    #valoresValidos          = models.BooleanField()
    #numeroPicos             = models.DecimalField(decimal_places=0,max_digits=3)
    #balanceIRRDC            = models.DecimalField(decimal_places=0,max_digits=3)

    # PRESION
    presion_actual          = models.DecimalField(decimal_places=0,max_digits=3)
    #pip                     = models.DecimalField(decimal_places=0,max_digits=3)
    #vt                      = models.DecimalField(decimal_places=0,max_digits=3)
    #frecuenciaRespitatoria  = models.DecimalField(decimal_places=0,max_digits=3)
    presion                 = models.JSONField()
    #volumen                 = models.JSONField()
    #flujo                   = models.JSONField()

    
    # funcion que devuelve una cadena de texto asociada al objeto
    def __str__(self):
        return self.modelo
    
    #def terapias_pendientes(self):
    #    return self.numero_terapias-self.terapias_realizadas