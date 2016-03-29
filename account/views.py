# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
import json
from db import models
def login(request):
    if request.method == 'GET':
        it = models.ShortMessage.objects.all()
        return HttpResponseRedirect('/')
    elif request.method == 'POST':
        #print request.POST['username'],request.POST['password']
        user_ =request.POST['username']
        pwd_ = request.POST['password']
        user = models.Member()
        flag = user.login(user_,pwd_)
        obj = {'result':'success'}
        obj1 = {'msg':'赵镇辉'}
        code = str(json.dumps(obj))
        code1 = str(json.dumps(obj1))
        if flag == True:
            return HttpResponse(code)
        elif flag == False:
            print "false"
            return HttpResponse(code1)
def register(request):
    
    pass