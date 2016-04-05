# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from db import common
from django.db.models import Q
from django.db import models
from compiler.pycodegen import EXCEPT
from django.utils import timezone
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

FirstRatio=0.05
SecondRatio=0.03
ThirdRatio=0.02
ONE_PAGE_OF_DATA = 5

class Advice(models.Model):
    advice_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Member', models.DO_NOTHING, db_column='user_id', blank=True, null=True)
    advice_title = models.CharField(max_length=20, blank=True, null=True)
    advice_content = models.CharField(max_length=255, blank=True, null=True)
    advice_created = models.DateTimeField(blank=True, null=True)
    reply_content = models.CharField(max_length=255, blank=True, null=True)
    reply_time = models.DateTimeField(blank=True, null=True)
    advice_status = models.CharField(max_length=1, blank=True, null=True)
    service = models.ForeignKey('Service', models.DO_NOTHING)
    #发送意见 advice_status = 0 为未阅读，1为已阅读
    def send_advice(self,user_id_,title_,content_,service_id_):
        try:
            time_ = timezone.now()
            Advice.objects.create(user_id = Member(user_id_), advice_title = title_, advice_content = content_,service = Service(service_id_)\
                                  ,advice_status = 0, advice_created = time_)
        except BaseException, e:
            print e
    def reply_advice(self,user_id_,reply_content_,service_id_,advice_id_):
        try:
            time_ = timezone.now()
            advice = Advice.objects.filter(advice_id = advice_id_).get()
            advice.advice_status = 1
            advice.reply_time = time_
            advice.reply_content = reply_content_
            advice.save()
            return True
        except BaseException, e:
            print e
            return False
    #我的意见role = 0为服务中心，=1为会员
    def my_advice(self,user_or_service_id_,role_="1",title_ = None,advice_status_ = None,\
                  time_start_ = None,time_end_ = None,pageNum=1):
        try:
            startPos = (pageNum-1)*ONE_PAGE_OF_DATA
            endPos = pageNum*ONE_PAGE_OF_DATA
            args = {}
            if role_ =="1":
                args['user_id'] = user_or_service_id_
            if role_ =="0":
                args['service_id'] = user_or_service_id_
            args1 = {}
            if title_ != None:
                args['advice_title'] = title_
            if advice_status_ != None:
                args['advice_status'] = advice_status_
            if time_start_ !=None:
                args['advice_created__gt'] = time_start_
            if time_end_ !=None:
                args1['advice_created__gt'] = time_end_
                adviceList = Advice.objects.filter(**args).exclude(**args1).all()[startPos:endPos]
                count = Advice.objects.filter(**args).exclude(**args1).count()
                return adviceList,(count/ONE_PAGE_OF_DATA)+1
            else:
                adviceList = Advice.objects.filter(**args).all()[startPos:endPos]
                count = Advice.objects.filter(**args).count()
                return adviceList,(count/ONE_PAGE_OF_DATA)+1
        except BaseException, e:
            print e
            return False

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
    #receiver_phone :收货人手机号 receiver_addr :收货地址  orderMemo:订单详情 serviceid:服务点ID referenceid推荐人ID 推荐人Id为0时为所在服务中心
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
                    #消息列表中增加一条
                    Message.objects.create(service_id = serviceid,message_title = nickname_+"首次加单，请审核订单并激活会员",\
                                           message_content ="会员"+nickname_+"已申请加单,请至会员列表进行审核。",\
                                           sent_time = time_, message_status = '0',user_id = i.user_id)
                    return True
                except BaseException,e:
                    print e
                    return False    
    #激活会员并且给会员发送已经激活消息
    def activateMember(self,user_id_,service_id_):
        try:
            i = Member.objects.filter(user_id = user_id_).get()
            i.status = MemberStatus(id = 2,status_id = '2')
            i.save()
            Message.objects.create(user_id = user_id_,message_title="您的帐号已激活",\
                                   message_content=i.user_name+"您已经被激活了推荐一个人就能进入公司公排系统，感谢您对我们的支持",message_status = 0,\
                                   sent_time = timezone.now())
            return True
        except BaseException,e:
            print e
            return False
    #会员页面中的我推荐的会员
    def myReference(self,user_id_,pageNum=1):
        startPos = (pageNum-1)*ONE_PAGE_OF_DATA
        endPos = pageNum*ONE_PAGE_OF_DATA
        args = []
        try:
            myReferenceList = Member.objects.filter(reference_id = user_id_ ).all()
            counts = Member.objects.filter(reference_id = user_id_ ).count()
            for i in myReferenceList:
                count = Member.objects.filter(reference_id = i.user_id ).count()
                args.append({"nickname":i.nickname,"phone":i.bind_phone,"reg_time":i.register_time,"conf_time":i.confirm_time,"ref_count":count})
                return args[startPos:endPos],(counts/ONE_PAGE_OF_DATA)+1
        except BaseException,e:
            print e
    #会员页面中我推荐的网络
    def myReferenceNet(self,user_id_,pageNum=1):
        try:
            startPos = (pageNum-1)*ONE_PAGE_OF_DATA
            endPos = pageNum*ONE_PAGE_OF_DATA
            args=[]
            myReferenceList = Member.objects.filter(reference_id = user_id_ ).all()
        except BaseException,e:
            print e
    #会员的会员网络
    #role = 0 为服务中心，= 1为会员默认为第一页
#     def myMemberNet(self,userOrServiceid_,role_,pageNum=1):
#         try:
#             startPos = (pageNum-1)*ONE_PAGE_OF_DATA
#             endPos = pageNum*ONE_PAGE_OF_DATA
#             if role_ == '0':
#                 memberlist = Member.objects.filter(reference_id = 0,service_id = userOrServiceid_).all()[startPos:endPos]
#                 count = Member.objects.filter(reference_id = 0,service_id = userOrServiceid_).count()
#                 print count
#                 return memberlist,(count/ONE_PAGE_OF_DATA)+1
#             if role_ == '1':
#                 memberlist = Member.objects.filter(reference_id = userOrServiceid_).all()[startPos:endPos]
#                 count = Member.objects.filter(reference_id = userOrServiceid_).count()
#                 return memberlist,(count/ONE_PAGE_OF_DATA)+1
#         except BaseException,e:
#             print e
            
            
class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    #id可以是userid或者是serviceid
    user_id = models.BigIntegerField(blank=True, null=True)
    service_id = models.BigIntegerField(blank=True, null=True)
    message_title = models.CharField(max_length=255, blank=True, null=True)
    message_content = models.CharField(max_length=255, blank=True, null=True)
    sent_time = models.DateTimeField(blank=True, null=True)
    #0表示未读，1表示为已读
    message_status = models.CharField(max_length=1, blank=True, null=True)
    #该函数只是改变了消息的状态 服务中心或用户阅读了该消息
    def readMessage(self,message_id_):
        try:
            time_ = timezone.now()
            msg = Message.objects.filter(message_id = message_id_).get()
            msg.message_status = 1
            msg.save()
            return True
        except BaseException,e:
            print e
            return False
    #message_status_ 为2表示所有消息 0表示未读，1表示为已读 role = 0 为会员,= 1为服务中心
    def myMessage(self,id_,role_,message_status_ = 2,pageNum = 1):
        try:
            startPos = (pageNum-1)*ONE_PAGE_OF_DATA
            endPos = pageNum*ONE_PAGE_OF_DATA
            if role_ == "0":
                if message_status_ == "2":
                    msglist = Message.objects.filter(user_id = id_).all()[startPos:endPos]
                    count = Message.objects.filter(user_id = id_).count()
                    return msglist,(count/ONE_PAGE_OF_DATA)+1
                else:
                    msglist = Message.objects.filter(user_id = id_,message_status = message_status_).all()[startPos:endPos]
                    count = Message.objects.filter(user_id = id_,message_status = message_status_).count()
                    return msglist,(count/ONE_PAGE_OF_DATA)+1
            elif role_ == "1":
                if message_status_ == "2":
                    msglist = Message.objects.filter(service_id = id_).all()[startPos:endPos]
                    count = Message.objects.filter(service_id = id_).count()
                    return msglist,(count/ONE_PAGE_OF_DATA)+1
                else:
                    msglist = Message.objects.filter(service_id = id_,message_status = message_status_).all()[startPos:endPos]
                    count = Message.objects.filter(service_id = id_,message_status = message_status_).count()
                    return msglist,(count/ONE_PAGE_OF_DATA)+1
        except BaseException,e:
            print e
    
class OrderForm(models.Model):
    order_id = models.AutoField(primary_key=True)
    service_id = models.BigIntegerField(blank=True, null=True)
    #0表示为未进入公排，1为进入公排系统
    order_valid_time = models.DateTimeField(blank=True, null=True)
    user_id = models.ForeignKey(Member, models.DO_NOTHING, db_column='user_id', blank=True, null=True)
    order_price = models.FloatField(blank=True, null=True)
    #0表示注册时加单，1表示为重复消费订单
    order_type = models.CharField(max_length=1, blank=True, null=True)
    order_created = models.DateTimeField(blank=True, null=True)
    order_finished = models.DateTimeField(blank=True, null=True)
    order_memo = models.CharField(max_length=100, blank=True, null=True)
    order_status = models.CharField(max_length=5, blank=True, null=True)
    express_name = models.CharField(max_length=20, blank=True, null=True)
    express_number = models.CharField(max_length=50, blank=True, null=True)
    def createOrder(self,service_id_,user_id_,order_price_,order_type_,order_memo_,order_status_="未发货"):
        try:
            OrderForm.objects.create(service_id = service_id_,user_id = Member(user_id = user_id_),order_price = order_price_,\
                                 order_type = order_type_,order_created = timezone.now(),order_memo = order_memo_,\
                                 order_status =order_status_)
            i = Member.objects.filter(user_id = user_id_).get()
            Message.objects.create(service_id = service_id_,message_title=i.user_name+"申请加单，请审核",\
                                   message_content=i.user_name+"已经申请加单，请至订单列表进行审核。",message_status = 0,\
                                   sent_time = timezone.now())
            return True
        except BaseException,e:
            print e
            return False
    #确认发货并且提醒会员已经发货了
    def comfirmDelivery(self,order_id_,express_name_,express_number_):
        try:    
            ord = OrderForm.objects.filter(order_id = order_id_).get()
            ord.express_name=express_name_
            ord.express_number=express_number_
            ord.order_status="已发货"
            ord.order_finished=timezone.now()
            ord.save()
            Message.objects.create(user_id = ord.user_id.user_id,message_title="您的订单已经发货",\
                                   message_content="您的商品"+ord.order_memo+"已经发货，快递号为"+express_number_,message_status = 0,\
                                   sent_time = timezone.now())
        except BaseException,e:
            print e
            return False
    #order_type 为0表示未发货的,1表示已发货的，2为所有 会员界面中我的订单
    def myMemberOrder(self,user_id_,start_time_=None,end_time_=None,order_type_="2",pageNum=1):
        startPos = (pageNum-1)*ONE_PAGE_OF_DATA
        endPos = pageNum*ONE_PAGE_OF_DATA
        try:
            arg={}
            args={}
            args['user_id']=user_id_
            if start_time_ !=None:
                args['order_created__gt']=start_time_
            if order_type_ == "0":
                args['order_status']='未发货'
            if order_type_ == "1":
                args['order_status']='已发货'
            if end_time_ !=None:
                arg['order_created__gt']=end_time_
                orderlist = OrderForm.objects.filter(**args).exclude(**arg).all()[startPos:endPos]
                count = OrderForm.objects.filter(**args).exclude(**arg).count()
                return orderlist,(count/ONE_PAGE_OF_DATA)+1
            elif end_time_ == None:
                orderlist = OrderForm.objects.filter(**args).all()[startPos:endPos]
                count = OrderForm.objects.filter(**args).count()
                return orderlist,(count/ONE_PAGE_OF_DATA)+1
        except BaseException,e:
            print e 
    #服务中心的订单 #order_type 为0表示未发货的,1表示已发货的，2为所有
    def myServiceOrder(self,service_id_,user_or_phone_=None,order_type_='2',start_time_=None,end_time_=None,pageNum=1):
        startPos = (pageNum-1)*ONE_PAGE_OF_DATA
        endPos = pageNum*ONE_PAGE_OF_DATA
        try:
            arg={}
            args={}
            args['service_id']=service_id_
            if user_or_phone_ !=None:
                #如果用户名或者绑定手机号给出
                i = Member.objects.filter(Q(user_name = user_or_phone_)|Q(bind_phone=user_or_phone_)).all()
                args['user_id'] = i.get().user_id
            if start_time_ !=None:
                args['order_created__gt']=start_time_
            if order_type_ == "0":
                args['order_status']='未发货'
            if order_type_ == "1":
                args['order_status']='已发货'
            if end_time_ !=None:
                arg['order_created__gt']=end_time_
                orderlist = OrderForm.objects.filter(**args).exclude(**arg).all()[startPos:endPos]
                count = OrderForm.objects.filter(**args).exclude(**arg).count()
                return orderlist,(count/ONE_PAGE_OF_DATA)+1
            elif end_time_ == None:
                orderlist = OrderForm.objects.filter(**args).all()[startPos:endPos]
                count = OrderForm.objects.filter(**args).count()
                return orderlist,(count/ONE_PAGE_OF_DATA)+1
        except BaseException,e:
            print e
    
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

