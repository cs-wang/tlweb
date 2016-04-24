# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
import json
from db import models
from urllib2 import Request
import hashlib
md5_used = False
def login(request):
    if request.method == 'GET':
        it = models.ShortMessage.objects.all()
        return HttpResponseRedirect('/')
    elif request.method == 'POST':
        user_ = request.POST['username']
        pwd_ = request.POST['password']    
        global md5_used
        if md5_used:
            pwd_ = hashlib.md5(pwd_.encode('utf8')).hexdigest()
        role_ = request.POST['role']
        print user_, pwd_,role_
        flag = models.Login(user_, pwd_, role_)
        if flag:
            request.session['role'] = role_
        obj = {'result':'success','role':role_}
        obj1 = {'msg':'登录失败'}
        obj2 = {'result':'success','role':'2'}
        code = str(json.dumps(obj))
        code1 = str(json.dumps(obj1))
        code2 = str(json.dumps(obj2))
        if flag == True:
            request.session['username'] = user_
            if role_ == '0':
                request.session['role'] = '0'
                request.session['user_id'] = models.Member.GetUser(user_).user_id
                request.session['username']=user_
            elif role_ == '1':
                request.session['role'] = '1'
                request.session['service_id'] = models.Service.GetService(user_).service_id
                sub_role = models.Service.GetService(user_).role
                if sub_role == '2':
                    request.session['role'] = '2'
                    subserviceobj = models.Service.GetService(user_)
                    request.session['service_id'] = subserviceobj.service_ref
                    request.session['subservice_id'] = subserviceobj.service_id
                    print "request.session['role']:",request.session['role']
                    print "request.session['service_id']:",request.session['service_id']
                    print "request.session['subservice_id']:",request.session['subservice_id']
                    return HttpResponse(code2)
            return HttpResponse(code)
        elif flag == False:
            return HttpResponse(code1)
         

def register(request, ReferenceId = None):

    if request.method == 'GET':
        member_ = models.Member()
  
        context ={}
        return render(request, 'Account/Register.html', context)
    elif request.method == 'POST':
        RegUserId = request.POST['UserId']
        RegUserName = request.POST['UserName']
        RegNickName = request.POST['NickName']
        RegIDCard = request.POST['IDCard']
        RegUserStatus = request.POST['UserStatus']
        RegBindMob = request.POST['BindMob']
        RegDepositMobile = request.POST['DepositMobile']
        RefMobile = request.POST['FromMobile']
        # md5 for password
        RegUserPwd = request.POST['UserPwd']
        global md5_used
        if md5_used:
            RegUserPwd = hashlib.md5(RegUserPwd.encode('utf8')).hexdigest()
        RegUserPayPwd = request.POST['UserPayPwd']
        RegWeChat = request.POST['WeChat']
        RegAlipay = request.POST['Alipay']
        RegBankName = request.POST['BankName']
        RegBankAccount = request.POST['BankAccount']
        RegTrueName = request.POST['TrueName']
        RegRecName = request.POST['RecName']
        RegRecAdd = request.POST['RecAdd']
        RegRecMob = request.POST['RecMob']
        RegMark = request.POST['Mark']
        
#         print "RefMobile:"
        '''
        print "RegUserId:",RegUserId
        print "RegUserName:",RegUserName
        print "RegNickName:",RegNickName
        print "RegIDCard:",RegIDCard
        print "RegUserStatus:",RegUserStatus
        print "RegBindMob:",RegBindMob
        print "RegDepositMobile:",RegDepositMobile
        print "RefMobile:",RefMobile
        print "RegUserPwd:",RegUserPwd
        print "RegUserPayPwd:",RegUserPayPwd
        print "RegWeChat:",RegWeChat
        print "RegAlipay:",RegAlipay
        print "RegBankName:",RegBankName
        print "RegBankAccount:",RegBankAccount
        print "RegTrueName:",RegTrueName
        print "RegRecName:",RegRecName
        print "RegRecAdd:",RegRecAdd
        print "RegRecMob:",RegRecMob
        print "RegMark:",RegMark
        '''
        memberobj = models.Member()
        try :
            with transaction.atomic():
                if memberobj.register(RegUserName,RegNickName,RefMobile,RegDepositMobile,RegAlipay,RegBindMob,RegUserPwd,RegWeChat,RegBankName,RegBankAccount,
                                      RegTrueName,RegRecName,RegRecMob,RegRecAdd,RegMark,1,0) == True:
                    obj = {'result':'t'}
                else:
                    obj = {'result':'f',
                               'msg':'用户名已经被注册,或推荐人手机号无效'}
        except BaseException,e:
            print e
            obj = {'result':'f','msg':'操作有误请重试'}
        code = str(json.dumps(obj))
        return HttpResponse(code)

def ChangePwd(request):
    context = {}
    if request.method == 'GET':
        context ={}
        return render(request, 'Account/ChangePwd.html', context)   
    elif request.method == 'POST':
        user_or_service_id_ = request.session['user_id']
        oldpwd_ = request.POST['OldPwd']
        newpwd_ = request.POST['NewPwd']
        role_id_ = request.session['role']
        print 'user_or_service_id_',user_or_service_id_
        print 'oldpwd_',oldpwd_
        print 'newpwd_',newpwd_
        print 'role_id_',role_id_
        flag = models.fixPwd(user_or_service_id_,oldpwd_,newpwd_,role_id_)
        print 'flag',flag
        if flag:
            obj = {'result':'t','msg':'修改成功'}
        else:
            obj = {'result':'f','msg':'请确认旧密码是否正确，副中心修改密码请联系服务中心'}
        code = str(json.dumps(obj))
        return HttpResponse(code)
