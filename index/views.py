from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'index/home.html', context)

def company(request):
    context = {}
    return render(request, 'index/company.html', context)

def product(request):
    context = {}
    return render(request, 'index/product.html', context)