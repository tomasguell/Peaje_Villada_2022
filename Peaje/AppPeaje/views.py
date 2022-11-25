from django.shortcuts import render, HttpResponseRedirect
from .forms import NuevoTurno
from datetime import datetime
from .models import turnos, operadores
# Create your views here.
from django.http import HttpResponseRedirect

from .forms import NuevoTicket

def index(request):
    context = {'key': 'hola'}
    return render(request, 'AppPeaje/dashboard.html', context=context)

def tickets(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NuevoTicket(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/tickets/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NuevoTicket()

    return render(request, 'AppPeaje/tickets.html', {'form': form})

def cargar_turnos(request):
    if request.method == 'POST':
        
        
        
        
        
        
        
        form = NuevoTurno(request.POST)
        
        if form.is_valid():
            
            fk_operador = operadores.objects.all().filter(usuario=request.user)[0]
            #print(fk_operador)
            #PROCESAR LA INFORMACION
            turno = form.save(commit=False)
            turno.fecha_creacion = datetime.now()
            turno.operador = fk_operador
            turno.save()
    else:
        form = NuevoTurno()
        
    
<<<<<<< HEAD
    
    return render(request, 'AppPeaje/turnos.html', {'form':form})
def informe(request):
    return render(request, 'AppPeaje/informe.html')
=======
    turnos_activos = turnos.objects.all().filter(turno_activo=True, operador__usuario = request.user)
        
    if len(turnos_activos) > 0:
        
        activar_form = False
        
    else:
        activar_form = True        
    return render(request, 'AppPeaje/turnos.html', {'form':form,
                                                    'activar_form':activar_form})

def terminar_turno(request):
    turnos_activos = turnos.objects.all().filter(turno_activo=True, operador__usuario = request.user)
    try:
        turno = turnos_activos[0]
        turno.turno_activo = False
        turno.fecha_fin = datetime.now()
        turno.save()
    except IndexError:
        pass    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
>>>>>>> fe7e031b14fbe873091708333fd79e75fd435b24
