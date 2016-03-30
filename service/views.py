from django.shortcuts import render

# Create your views here.

def home(request):
    context = { }
    return render(request, 'service/home.html', context)

def anounce(request):
    context = { }
    return render(request, 'service/anounce.html', context)

def message(request):
    context = { }
    return render(request, 'service/message.html', context)
    
def register(request):
    context = { }
    return render(request, 'service/register.html', context) 
    