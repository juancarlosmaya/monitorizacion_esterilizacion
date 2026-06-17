"""electroestimulador_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# REST API
from rest_framework import routers
from .views import vista_examinar_esterilizador
router = routers.DefaultRouter()
router.register('esterilizador', vista_examinar_esterilizador)




from django.contrib import admin
#from django.urls import path

# archivos estaticos como .css
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# paginas de inicio y acerca de
from .views import pagina_inicio 


# para importar urls de otras aplicaciones
from django.urls import path, include, re_path

urlpatterns = [
    # página de administración
    path('admin/', admin.site.urls),
    
    # páginas de incio
    path('',pagina_inicio,name='pagina_inicio'), 
    
    # pagina de revisar pacientes
    path('revisar/', include('revisar_esterilizadores.urls')),

    # página de gestión de pacientes
    path('gestion/', include('gestion_esterilizadores.urls')),

    # página de simulación de uso de lavadora
    path('simulador/', include('simulador_oximetria.urls')),

    re_path(r'^API', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += staticfiles_urlpatterns()