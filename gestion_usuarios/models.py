
from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre                  = models.CharField(max_length=20)
    cedula                  = models.DecimalField(decimal_places=0,max_digits=12)
    fecha_nacimiento        = models.DateField()
    frecha_registro         = models.DateField()

    conectado               = models.BooleanField()    

    # OXIMETRÍA
    oximetria               = models.DecimalField(decimal_places=0,max_digits=3)
    frecuenciaCardiaca      = models.DecimalField(decimal_places=0,max_digits=3)
    pletismografia          = models.JSONField()
    valoresValidos          = models.BooleanField()
    numeroPicos             = models.DecimalField(decimal_places=0,max_digits=3)
    balanceIRRDC            = models.DecimalField(decimal_places=0,max_digits=3)

    # VENTILACIÓN
    fiO2                    = models.DecimalField(decimal_places=0,max_digits=3)
    pip                     = models.DecimalField(decimal_places=0,max_digits=3)
    vt                      = models.DecimalField(decimal_places=0,max_digits=3)
    frecuenciaRespitatoria  = models.DecimalField(decimal_places=0,max_digits=3)
    presion                 = models.JSONField()
    volumen                 = models.JSONField()
    flujo                   = models.JSONField()

    
    # funcion que devuelve una cadena de texto asociada al objeto
    def __str__(self):
        return self.nombre
    
    #def terapias_pendientes(self):
    #    return self.numero_terapias-self.terapias_realizadas