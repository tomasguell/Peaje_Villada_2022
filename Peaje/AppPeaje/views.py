from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'key': 'hola'}
    return render(request, 'AppPeaje/index.html', context=context)

