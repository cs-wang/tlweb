# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from db import common
from django.db import models
from compiler.pycodegen import EXCEPT
from django.utils import timezone

class Advice(models.Model):
    advice_id = models.AutoField(primary_key=True)
    user_name = models.ForeignKey('Member', models.DO_NOTHING, db_column='user_name', blank=True, null=True)
    advice_content = models.CharField(max_length=255, blank=True, null=True)
    advice_created = models.DateTimeField(blank=True, null=True)
    reply_time = models.DateTimeField(blank=True, null=True)
    service = models.ForeignKey('Service', models.DO_NOTHING)

class CommissionDetail(models.Model):
    commission_type = models.CharField(primary_key=True, max_length=1)
    commission_desc = models.CharField(max_length=10, blank=True, null=True)

class CommissionOrder(models.Model):
    commission_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Member', models.DO_NOTHING, db_column='user_id')
    commission_price = models.FloatField(blank=True, null=True)
    commission_type = models.ForeignKey(CommissionDetail, models.DO_NOTHING, db_column='commission_type')
    commission_memo = models.CharField(max_length=255, blank=True, null=True)
    commission_created = models.DateTimeField(blank=True, null=True)
    commission_sent = models.DateTimeField(blank=True, null=True)
    commission_status = models.CharField(max_length=1, blank=True, null=True)

class MemberStatus(models.Model):
     status_id = models.CharField(max_length=1)
     status_desc = models.CharField(max_length=20)

class Member(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    nickname = models.CharField(max_length=10)
    status = models.ForeignKey('MemberStatus', models.DO_NOTHING)
    service_id = models.BigIntegerField(blank=True, null=True)
    reference_id = models.BigIntegerField(blank=True, null=True)
    delegation_phone = models.CharField(max_length=20, blank=True, null=True)
    delegation_info = models.CharField(max_length=100, blank=True, null=True)
    bind_phone = models.CharField(max_length=20)
    weixin_id = models.CharField(max_length=50, blank=True, null=True)
    bank = models.CharField(max_length=255)
    account = models.CharField(max_length=50)
    card_holder = models.CharField(max_length=20, blank=True, null=True)
    receiver = models.CharField(max_length=20, blank=True, null=True)
    receiver_phone = models.CharField(max_length=20, blank=True, null=True)
    receiver_addr = models.CharField(max_length=255, blank=True, null=True)
    register_time = models.DateTimeField(blank=True, null=True)
    confirm_time = models.DateTimeField(blank=True, null=True)
 
    #user用户名 pwd密码 role角色 0为会员1为服务点
    def login(self,user,pwd,role):
         print role
         if role == '0':
             try:
                 userEntity = Member.objects.filter(user_name = user).get()
                 if userEntity.password == pwd:
                     return True
                 else:
                     return False
             except BaseException, e:
                 return False
         elif role == '1':
             try:
                 serviceEntity = Service.objects.filter(service_name = user).get()
                 if serviceEntity.service_pwd == pwd:
                     return True
                 else:
                     return False
             except BaseException, e:
                 return False
    #user :用户名 nickname：昵称或姓名 delegation_phone委托汇款人手机号 delegation_info委托汇款信息 
    #bind_phone:绑定手机 pwd:密码 weixinId:微信号 bank:开户银行 account:卡号 cardHolder:持卡人 receiver:收货人
    #receiver_phone :收货人手机号 receiver_addr :收货地址  orderMemo:订单详情 serviceid:服务点ID referenceid推荐人ID
    #同时修改会员表和订单表
    def register(self,user,nickname_,delegation_phone_,delegation_info_,\
         bind_phone_,pwd,weixinId,bank_,account_,cardHolder,receiver_,reciever_phone_,\
         receiver_addr_,order_Memo_,serviceid,referenceid):
            
            userEntity = Member.objects.filter(user_name = user)
            if len(userEntity) >= 1:
                print "用户名已经被注册"
                return False
            else:
                try:
                    print "hello" 
                    #获取id最大值
                    time_ = timezone.now()
                    #修改member表
                    i = Member.objects.create(user_name = user,password = pwd,nickname = nickname_,\
                                          status_id = 1,service_id = serviceid,reference_id = referenceid,\
                                          delegation_phone = delegation_phone_,\
                                          delegation_info = delegation_info_,bind_phone = bind_phone_,\
                                          weixin_id = weixinId,bank = bank_,account = account_,card_holder = cardHolder,\
                                          receiver = receiver_,receiver_phone = reciever_phone_,receiver_addr = receiver_addr_,\
                                          register_time = time_)
                    #修改订单表
                    OrderForm.objects.create(service_id = serviceid , user_id = Member(user_id = i.user_id),\
                                             order_price = 1000, order_type = 0,order_created = time_,order_memo = order_Memo_,\
                                             order_status ="未发货" )
                    print "注册成功"
                except BaseException,e:
                    print e
                pass    

class Message(models.Model):
    message_id = models.BigIntegerField(primary_key=True)
    message_title = models.CharField(max_length=255, blank=True, null=True)
    message_content = models.CharField(max_length=255, blank=True, null=True)
    sent_time = models.DateTimeField(blank=True, null=True)
    message_status = models.CharField(max_length=1, blank=True, null=True)

class OrderForm(models.Model):
    order_id = models.AutoField(primary_key=True)
    service_id = models.BigIntegerField(blank=True, null=True)
    order_rank = models.BigIntegerField(blank=True, null=True)
    user_id = models.ForeignKey(Member, models.DO_NOTHING, db_column='user_id', blank=True, null=True)
    order_price = models.FloatField(blank=True, null=True)
    order_type = models.CharField(max_length=1, blank=True, null=True)
    order_created = models.DateTimeField(blank=True, null=True)
    order_finished = models.DateTimeField(blank=True, null=True)
    order_memo = models.CharField(max_length=100, blank=True, null=True)
    order_status = models.CharField(max_length=5, blank=True, null=True)
    express_name = models.CharField(max_length=20, blank=True, null=True)
    express_number = models.CharField(max_length=50, blank=True, null=True)
     
class Product(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_price = models.FloatField(blank=True, null=True)
 
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=20)
    service_pwd = models.CharField(max_length=32, blank=True, null=True)
    service_area = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=1, blank=True, null=True)
    
class ServiceAccount(models.Model):
    service = models.ForeignKey(Service, models.DO_NOTHING)
    bank = models.CharField(primary_key=True, max_length=255)
    bank_account = models.CharField(max_length=50, blank=True, null=True)
    card_holder = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

class ShortMessage(models.Model):
    message_id = models.IntegerField(primary_key=True)
    message_content = models.CharField(max_length=200, blank=True, null=True)

