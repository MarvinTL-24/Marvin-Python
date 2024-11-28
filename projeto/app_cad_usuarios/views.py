from django.shortcuts import render

def home(request):
    return render(request, 'usuario/home.html')

# Adicionado aqui
def usuarios(request):
    pass
