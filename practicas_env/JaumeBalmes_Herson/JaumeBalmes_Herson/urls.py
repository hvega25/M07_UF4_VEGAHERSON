#Librerias importadas
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #urls de las aplicaciones creadas
    #url de la aplicación alumnos
    path('alumnos/', include('alumnos.urls')),
    #url de la aplicación profesores
    path('profesores/', include('profesores.urls'))
]
