from django.shortcuts import render

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