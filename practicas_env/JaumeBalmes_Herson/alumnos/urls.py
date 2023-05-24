from django.urls import path
from . import views


#Rutas de la aplicación
urlpatterns=[
    #url de la aplicacion
    path('alumnos/', views.alum, name='alumno')
]