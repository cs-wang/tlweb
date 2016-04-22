# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
import json
from db import models
from urllib2 import Request
def login(request):
    if request.method == 'GET':
        it = models.ShortMessage.objects.all()
        return HttpResponseRedirect('/')
    elif request.method == 'POST':
        user_ = request.POST['username']
        pwd_ = request.POST['password']    
        role_ = request.POST['role']
        print user_, pwd_,role_
        member_ = models.Member()
        flag = member_.login(user_,pwd_,role_)
        print flag,'hello'
        obj = {'result':'success','role':role_}
        obj1 = {'msg':'登录失败'}
        code = str(json.dumps(obj))
        code1 = str(json.dumps(obj1))
        if flag == True:
            user_id=member_.getUserId(user_).user_id
            request.session['user_id']=user_id
            request.session['username']=user_
            if role_ == '0':
                request.session['role'] = '0'
            elif role_ == '1':
                request.session['role'] = '1'
            return HttpResponse(code)
        elif flag == False:
            return HttpResponse(code1)
         
def register(request):
    member_ = models.Member()
    #有推荐人
#     flag = member_.register('new',"hahah","delegation_phone_","delegation_info_",\
#           "bind_phone_","pwd","weixinId","bank_","account_","cardHolder","receiver_","reciever_phone_",\
#           "receiver_addr_","order_Memo",1,1)
    context ={}
    return render(request, 'index/home.html', context)
#     return HttpResponse("ok")