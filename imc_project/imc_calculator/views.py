from django.shortcuts import render

def calcular_imc(request):
    imc = None
    classificacao = ""

    if request.method == "POST":
        peso = float(request.POST.get("peso"))
        altura = float(request.POST.get("altura"))
        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            classificacao = "Peso normal"
        elif 25 <= imc < 29.9:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

    return render(request, "imc_calculator/index.html", {"imc": imc, "classificacao": classificacao})
