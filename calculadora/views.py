from django.shortcuts import render

def calcular_promedio(request):
    promedio = None 

    if request.method == "POST":
        try:
            nota1 = float(request.POST.get('nota1'))
            nota2 = float(request.POST.get('nota2'))
            nota3 = float(request.POST.get('nota3'))
            nota4 = float(request.POST.get('nota4'))

            promedio = round((nota1 + nota2 + nota3 + nota4) / 4, 2)

        except (TypeError, ValueError):
            promedio = "Error: Ingresa solo números válidos"

    return render(request, 'calculadora/formulario.html', {'promedio': promedio})

