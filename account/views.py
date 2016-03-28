from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
import json
def login(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    elif request.method == 'POST':

        print request.POST['username'],request.POST['password']
        obj = {'result':'success'}
        code = str(json.dumps(obj))
        return HttpResponse(code)
    
def register(request):
    
    pass