#Librerias importadas
from django.contrib import admin
from django.urls import path,include
from alumnos  import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #urls de las aplicaciones creadas
    #ruta principal
    path('' , views.home , name="home"),
    #url de la aplicación alumnos
    path('alumnos/', include('alumnos.urls'),  name='alumnos'),
    #url de la aplicación profesores
    path('profesores/', include('profesores.urls'), name='profesores')
]
