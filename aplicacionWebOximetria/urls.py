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
from .views import vista_examinar_usuario
router = routers.DefaultRouter()
router.register('usuario', vista_examinar_usuario)



from django.contrib import admin
#from django.urls import path

# archivos estaticos como .css
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# paginas de inicio y acerca de
from .views import pagina_inicio 


# para importar urls de otras aplicaciones
from django.conf.urls import url,include
from django.urls import path

urlpatterns = [
    # página de administración
    url(r'^admin/', admin.site.urls),
    
    # páginas de incio
    url(r'^$',pagina_inicio,name='pagina_inicio'), 
    
    # pagina de revisar pacientes
    url(r'^revisar/', include('revisar_usuarios.urls')),

    # página de gestión de pacientes
    url(r'^gestion/', include('gestion_usuarios.urls')),

    # página de simulación de uso de lavadora
    url(r'^simulador/', include('simulador_oximetria.urls')),

    # prueba de plantilla boostrap dashboard
    path('django-sb-admin/', include('django_sb_admin.urls')),

    url(r'API', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += staticfiles_urlpatterns()