from django.shortcuts import render
from boto.connection import HTTPResponse

def home(request):
    context = {}
    return render(request, 'Index/home.html', context)

def company(request):
    context = {}
    return render(request, 'Index/company.html', context)

def product(request):
    context = {}
    return render(request, 'Index/product.html', context)
def page(request):
    context = {}
    
    return render(request, 'Index/pageTest.html', context)

def page404(request):
    
    return HTTPResponse("444")