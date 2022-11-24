from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'key': 'hola'}
    return render(request, 'AppPeaje/dashboard.html', context=context)

def tickets(request):
    return render(request, 'AppPeaje/tickets.html')


