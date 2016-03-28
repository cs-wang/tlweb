from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'home.html', context)

def company(request):
    context = {}
    return render(request, 'company.html', context)

def product(request):
    context = {}
    return render(request, 'product.html', context)