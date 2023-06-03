from django.urls import path
from . import views


#Rutas de la aplicación
urlpatterns=[
    #url de la aplicacion
    path('alumnos/', views.alum, name='alumno'),
    path('alumno-form/', views.alumno_form , name='alumno_form'),

    #url para listar alumnos de la base de datos
    path('listar/' , views.listar , name='lista_alumnos'),
    #url para actualizar datos
    path('update-alumno/<str:pk>/', views.update_alumno , name='update-alumno'),
    #url para eliminar un elemento
    path('delete-alumno/<str:pk>/' , views.delete_alumno, name='delete-alumno')
]