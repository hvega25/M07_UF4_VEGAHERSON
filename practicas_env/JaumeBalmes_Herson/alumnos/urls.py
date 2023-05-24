from django.urls import path
from . import views


#Rutas de la aplicación
urlpatterns=[
    #url de la aplicacion
    path('student/', views.alum, name='alumno')
]