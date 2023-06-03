from django.shortcuts import render, redirect

#incluyento la libreria form
from .forms import AlumnoForm

#importar models 

from .models import alumnos

#Método que sea la página principal
def home (request):
    return render(request, 'index.html')

#Método que devuelve los datos de los alumnos
def alum (request):
    alumnes = {
        'alumno 1': { "id": "1","name": "herson" , "surname": "vega", "age": "27"},
        'alumno 2': {"id": "2","name": "xavier", "surname": "garay", "age": "26"},
        'alumno 3': {"id": "3","name": "lena", "surname": "paul", "age": "27"},
        'alumno 4': {"id": "4","name": "herson", "surname": "vega", "age": "27"},
        'alumno 5': {"id": "5","name": "herson", "surname": "vega", "age": "27"},
        'alumno 6': {"id": "6","name": "herson", "surname": "vega", "age": "27"},
    }
    context = {'alu': alumnes}
    return render(request, 'alumno.html', context)


#Método de de alumno
def alumno_form(request):
    form = AlumnoForm()

    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno_listar.html')
    context = {'form': form}
    return render (request, 'alumno_form.html', context)


#vista para lectura de base de datos
def listar (request):
    student = alumnos.objects.all()
    return render(request, "alumno_listar.html", {"alum":student})