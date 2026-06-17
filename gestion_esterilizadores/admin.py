from django.contrib import admin


# Register your models here.

from .models import Esterilizador

# registra la base de daos en sitio admin
admin.site.register(Esterilizador)