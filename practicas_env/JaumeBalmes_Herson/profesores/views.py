from django.shortcuts import render

#Método que devuelve los datos de los profesores
def prof (request):
    profesores = {
        'profesor 1': {"id": "1", "name": "herson" , "surname": "vega", "age": "27"},
        'profesor 2': {"id": "2","name": "xavier", "surname": "garay", "age": "26"},
        'profesor 3': {"id": "3","name": "lena", "surname": "paul", "age": "27"},
    }
    context = {'prf': profesores}
    return render(request, 'profesor.html', context)
