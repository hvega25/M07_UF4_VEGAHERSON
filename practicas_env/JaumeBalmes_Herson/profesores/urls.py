from django.urls import path
from . import views

#Rutas de la aplicación
urlpatterns=[
    #url de la aplicación
    path('teachers/', views.prof, name='teacher')
]