from django.shortcuts import render
from .forms import NuevoTurno
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

def turnos(request):
    if request.method == 'POST':
        form = NuevoTurno(request.POST)
        
        if form.is_valid():
            #PROCESAR LA INFORMACION
            print(form)
    else:
        form = NuevoTurno()
    
    
    return render(request, 'AppPeaje/turnos.html', {'form':form})
