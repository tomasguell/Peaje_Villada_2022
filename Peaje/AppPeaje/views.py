from django.shortcuts import render
from .forms import NuevoTurno
# Create your views here.

def index(request):
    context = {'key': 'hola'}
    return render(request, 'AppPeaje/dashboard.html', context=context)

def tickets(request):
    return render(request, 'AppPeaje/tickets.html')

def turnos(request):
    if request.method == 'POST':
        form = NuevoTurno(request.POST)
        
        if form.is_valid():
            #PROCESAR LA INFORMACION
            print(form)
    else:
        form = NuevoTurno()
    
    
    return render(request, 'AppPeaje/turnos.html', {'form':form})
