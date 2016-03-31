# -*- coding: utf-8 -*- 
from django.shortcuts import render
from db import models
from _ast import Return
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
#     if request.method == 'GET':
#         return 
#     elif request.method == 'POST':
#         return
    member_ = models.Member()
#     flag = member_.register('sb',"nickname_","delegation_phone_","delegation_info_",\
#          "bind_phone_","pwd","weixinId","bank_","account_","cardHolder","receiver_","reciever_phone_",\
#          "receiver_addr_","order_Memo",1,0)     
    context = { }
    return render(request, 'service/register.html', context) 
    