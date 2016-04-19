# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from db import common
from django.db.models import Q
import datetime
from django.db import models
from compiler.pycodegen import EXCEPT
from django.utils import timezone
import sys
from scipy.constants.constants import year
reload(sys)
sys.setdefaultencoding('utf-8')

FirstRatio = 0.05
SecondRatio = 0.03
ThirdRatio = 0.02
tax = 0.05
ONE_PAGE_OF_DATA = 15    

#user用户名 pwd密码 role角色 0为会员1为服务点
def Login(user,pwd,role):
    if role == '0':
         try:
             userEntity = Member.objects.filter(user_name = user).get()
             if userEntity.password == pwd and role !='5':
                 return True
             else:
                 return False
         except BaseException, e:
             print e
             return False
    elif role == '1':
         try:
             serviceEntity = Service.objects.filter(service_name = user).get()
             print serviceEntity
             #副中心禁用时不行
             if serviceEntity.service_pwd == pwd and serviceEntity.role !='3':
                 return True
             else:
                 return False
         except BaseException, e:
             print e
             return False

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
    #发送意见 advice_status = 0 为未阅读，1为已阅读2为所有
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
            if advice_status_ != None and advice_status_ !='2':
                args['advice_status'] = advice_status_
            if time_start_ !=None:
                args['advice_created__gt'] = time_start_
            if time_end_ !=None:
                args1['advice_created__gt'] = time_end_
                adviceList = Advice.objects.filter(**args).exclude(**args1).all()[startPos:endPos]
                count = Advice.objects.filter(**args).exclude(**args1).count()
                if count%ONE_PAGE_OF_DATA == 0:
                    return adviceList,(count/ONE_PAGE_OF_DATA),count
                else:
                    return adviceList,(count/ONE_PAGE_OF_DATA)+1,count
            else:
                adviceList = Advice.objects.filter(**args).all()[startPos:endPos]
                count = Advice.objects.filter(**args).count()
                if count%ONE_PAGE_OF_DATA == 0:
                    return adviceList,(count/ONE_PAGE_OF_DATA),count
                else:
                    return adviceList,(count/ONE_PAGE_OF_DATA)+1,count
        except BaseException, e:
            print e
            return [],0,0

    def one_advice(self, adv_id_):
    	advice = Advice.objects.filter(advice_id = adv_id_).get()
    	return advice
class CommissionDetail(models.Model):
    commission_type = models.CharField(primary_key=True, max_length=1)
    commission_desc = models.CharField(max_length=10, blank=True, null=True)

class CommissionOrder(models.Model):
    commission_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Member', models.DO_NOTHING, db_column='user_id')
    service_id = models.BigIntegerField(blank=True, null=True)
    commission_price = models.FloatField(blank=True, null=True)
    #0为推荐奖，1为优秀推荐奖，2超级推荐奖，3为广告费(层奖)，4为网络推荐奖，5为优秀人才奖
    commission_type = models.ForeignKey(CommissionDetail, models.DO_NOTHING, db_column='commission_type')
    commission_memo = models.CharField(max_length=255, blank=True, null=True)
    commission_created = models.DateTimeField(blank=True, null=True)
    commission_sent = models.DateTimeField(blank=True, null=True)
    #佣金状态有三种 0待审核 1待发放 2已发放 
    commission_status = models.CharField(max_length=1, blank=True, null=True)
    #佣金发放查询列表
    def commissionList(self,user_name_=None,commission_status_=None,commission_type_=None,commision_created_start_=None,commision_created_end_=None,time_order_='0',pageNum=1):
        args = {}
        arg ={}
        comlist = []
        orderlist = {'0':'commission_created','1':'-commission_created','2':'-commission_sent','3':'-commission_sent'}
        startPos = (pageNum-1)*ONE_PAGE_OF_DATA
        endPos = pageNum*ONE_PAGE_OF_DATA
        money = 0
        if user_name_ !=None:
            i = Member.objects.filter(user_name = user_name_).get()
            args['user_id'] = i.user_id
        if commission_status_ !=None:
            args['commission_status'] = commission_status_
        if commission_type_ != None:
            args['commission_type'] = commission_type_
        if commision_created_start_ != None:
            args['commission_created__gt'] = commision_created_start_
        if commision_created_end_ != None:
            arg['commission_created__gt'] = commision_created_end_
            comlist = CommissionOrder.objects.filter(**args).exclude(**arg).order_by(orderlist.get(time_order_)).all()[startPos:endPos]
            count = CommissionOrder.objects.filter(**args).exclude(**arg).count()
            for i in comlist:
                money = money + i.commission_price
            if count%ONE_PAGE_OF_DATA == 0:
                return comlist,(count/ONE_PAGE_OF_DATA),count,money
            else:
                return comlist,(count/ONE_PAGE_OF_DATA)+1,count,money
        else:
            comlist = CommissionOrder.objects.filter(**args).order_by(orderlist.get(time_order_)).all()[startPos:endPos]
            count = CommissionOrder.objects.filter(**args).count()
            for i in comlist:
                money = money + i.commission_price
            if count%ONE_PAGE_OF_DATA == 0:
                return comlist,(count/ONE_PAGE_OF_DATA),count,money
            else:
                return comlist,(count/ONE_PAGE_OF_DATA)+1,count,money
    
    #审核佣金单
    def confirmComm(self,commission_id_):
        try:
            com = CommissionOrder.objects.filter(commission_id = commission_id_).get()
            if com.commission_status == '0':
                com.commission_status = '1'
                com.save()
                return True
        except BaseException,e:
            print e
            return False
   
    #发放佣金单
    def deliverComm(self,commission_id_):
        try:
            com = CommissionOrder.objects.filter(commission_id = commission_id_).get()
            if com.commission_status == '1':
                com.commission_status = '2'
                com.save()
                return True
        except BaseException,e:
            print e
            return False
    #领导奖获得所有下级上个月所得
    def leadercommission(self,service_id_):
        #获取当前时间
#         time = timezone.now()
        time = datetime.datetime(2016,5,20)
        time_1 = datetime.datetime(time.year,time.month,01)
        if time.month == 1:
            time_2 = datetime.datetime(time.year-1,12,01)
        else:
            time_2 = datetime.datetime(time.year,time.month-1,01)
        #查询上个月是否已经生成领导奖订单
        if CommissionOrder.objects.filter(service_id = service_id_).filter(commission_type = CommissionDetail(commission_type = '7')).filter(commission_created__gt =time_2).exclude(commission_created__gt =time_1).count() == 0:            
            list = Member.objects.filter(service_id = service_id_).all()
            for i in list:
                count = Member.objects.filter(reference_id = i.user_id ).count()
                if count >0:
                    myReferenceList = Member.objects.filter(reference_id = i.user_id ).all()
                    money = 0
                    #对所有孩子的上月推荐奖订单
                    for j in myReferenceList:
                        commissionlists = CommissionOrder.objects.filter(user_id = j.user_id).\
                                filter(commission_created__gt =time_2).\
                                filter(Q(commission_type = CommissionDetail(commission_type = '0'))\
                                       |Q(commission_type = CommissionDetail(commission_type = '1'))\
                                       |Q(commission_type = CommissionDetail(commission_type = '2')))\
                                       .exclude(commission_created__gt =time_1).all()
                        if commissionlists.count() >0:
                            for k in commissionlists:
                                money = money +k.commission_price
#                     print i.user_id,"获得",money
                    if money >0:
                        CommissionOrder.objects.create(user_id = Member(user_id = i.user_id),commission_price = money*0.1,\
                                               commission_created = timezone.now(),commission_status = '0',\
                                               commission_type = CommissionDetail(commission_type = '7'),service_id =i.service_id)
                else:
                    pass
        else:
            print "已经生成"
    # 服务点上个月最优秀10人
    # 暂时不需要
    #传入当前时间 timezone.now()
#     def bestTenPeople(self,service_id_):
#         time = timezone.now()
# #         time = datetime.datetime(2016,5,20)
#         month=0
#         year = time.year
#         name_list = []
#         ref_num_list = []
#         if (time.month in [1,3,5,7,8,10,12]):
#             #day为上个月最后一天
#             day = 30
#         else :
#             day = 31
#         if (time.month == 1):
#             year = time.year-1
#             month = 12
#         else:
#             month = time.month-1
#         if time.year%400 == 0 or (time.year%4==0 and time.year%100 !=0):
#             if(month == 2):
#                 day = 29
#         else:
#             if(month == 2):
#                 day = 28
#         start_day = datetime.datetime(year,month,01)
#         end_day = datetime.datetime(year,month,day)
#         for p in CommissionOrder.objects.raw("SELECT commission_id,user_id,count(user_id) max_id FROM tldb.db_commissionorder\
#                                                     where service_id = %s and commission_created >='%s-%s-01' and commission_created<='%s-%s-%s' \
#                                                     group by user_id order by max_id Desc"%(service_id_,year,month,year,month,day)):
#             name_list.append(p.user_id.user_name)
#             ref_num_list.append(p.max_id)
#         
#         length = len(ref_num_list)
#         print length
#         if length<=10:
#             print "不足10个，不做处理全部返回"
#             return name_list,ref_num_list
#         else:
#             for i in range(10,length):
#                 if ref_num_list[i-1] == ref_num_list[i]:
#                     pass
#                 else: 
#                     break
#             if i == 10 : 
#                 return name_list[0:i],ref_num_list[0:i]
#             else :
#                 return name_list[0:i+1],ref_num_list[0:i+1]

    #达到优秀推荐和超级推荐
    def getGreatOrSuper(self,user_id_):
        time = timezone.now()
        time_1 = datetime.datetime(time.year,time.month,1)
        arg={}
        args={}
        arg['commission_created__gt'] = time
        args['commission_created__gt'] = time_1
        args['user_id'] =user_id_
        normal = CommissionOrder.objects.exclude(**arg).\
        filter(**args).filter(Q(commission_type = CommissionDetail(commission_type = '0'))\
                              |Q(commission_type = CommissionDetail(commission_type = '6'))).count()
        great = CommissionOrder.objects.exclude(**arg).filter(**args).\
            filter(commission_type = CommissionDetail(commission_type = '1')).count()
        super = CommissionOrder.objects.exclude(**arg).filter(**args).\
            filter(commission_type = CommissionDetail(commission_type = '2')).count()
        print normal,great,super
        
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
 
    #修改密码
    def fixMemberPwd(self,user_id_,old_pwd,new_pwd):
        try:
            userEntity = Member.objects.filter(user_id = user_id_).get()
            if userEntity.password == old_pwd:
                userEntity.password = new_pwd
                userEntity.save()
                return True
            else :
                return False
        except BaseException,e:
            print e
    #user用户名 pwd密码 role角色 0为会员1为服务点
#     def login(self,user,pwd,role):
#          if role == '0':
#              try:
#                  userEntity = Member.objects.filter(user_name = user).get()
#                  if userEntity.password == pwd and role !='5':
#                      return True
#                  else:
#                      return False
#              except BaseException, e:
#                  print e
#                  return False
#          elif role == '1':
#              try:
#                  serviceEntity = Service.objects.filter(service_name = user).get()
#                  print serviceEntity
#                  #副中心禁用时不行
#                  if serviceEntity.service_pwd == pwd and serviceEntity.role !='3':
#                      return True
#                  else:
#                      return False
#              except BaseException, e:
#                  print e
#                  return False
             
    #user :用户名 nickname：昵称或姓名 delegation_phone委托汇款人手机号 delegation_info委托汇款信息 
    #bind_phone:绑定手机 pwd:密码 weixinId:微信号 bank:开户银行 account:卡号 cardHolder:持卡人 receiver:收货人
    #receiver_phone :收货人手机号 receiver_addr :收货地址  orderMemo:订单详情 serviceid:服务点ID referenceid推荐人ID 推荐人Id为0时为所在服务中心
    #同时修改会员表和订单表
    def register(self,user,nickname_,delegation_phone_,delegation_info_,\
         bind_phone_,pwd,weixinId,bank_,account_,cardHolder,receiver_,reciever_phone_,\
         receiver_addr_,order_Memo_,serviceid,referenceid):
            
            userEntity = Member.objects.filter(user_name = user)
            if len(userEntity) >= 1:
                print "已经存在用户"
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
                    print i.user_id,"注册成功"
                    send_Short_Message(bind_phone_, "恭喜您已审核通过成为天龙健康会员，你的注册号："+user+\
                                       "，推荐会员可以获得公司推广奖励，详见奖励模式请登录www.tljk518.com.回复TD退订【天龙健康】")
                    #修改订单表
                    OrderForm.objects.create(service_id = serviceid , user_id = Member(user_id = i.user_id),\
                                             order_price = 1000, order_type = 0,order_created = time_,order_memo = order_Memo_,\
                                             order_status ="未发货")
                    #消息列表中增加一条
                    Message.objects.create(service_id = serviceid,message_title = nickname_+"首次加单，请审核订单并审核会员",\
                                           message_content ="会员"+nickname_+"已申请加单,请至会员列表进行审核。",\
                                           sent_time = time_, message_status = '0',user_id = i.user_id)
                    return True
                except BaseException,e:
                    print e
                    return False    
    #激活会员并且给会员发送已经激活消息
#     @staticmethod
#     def activateMember(user_id_,service_id_):
#         try:
#             i = Member.objects.filter(user_id = user_id_).get()
#             i.status = MemberStatus(id = 3,status_id = '3')
#             i.save()
# 
#             return True
#         except BaseException,e:
#             print e
#             return False
    #会员是申请加单，或者未审核时，收到钱后去审核
    #审核会员并且给会员发送已经审核消息
    #暂时不用，该版本为2叉树
#     def confirmMember(self,user_id_,service_id_):
#         try:
#             i = Member.objects.filter(user_id = user_id_).get()
# #             print i.user_name,i.status_id
#             #不是未审核或申请加单就无法被审核
#             if i.status.status_id == "1" or i.status.status_id == "7":
#                 i.status = MemberStatus(id = 2,status_id = '2')
#                 i.confirm_time = timezone.now()
#                 i.save()
#                 Message.objects.create(user_id = user_id_,message_title="您的帐号通过审核",\
#                                     message_content=i.user_name+"您已经通过审核推荐一个人就能进入公司公排系统，感谢您对我们的支持",message_status = 0,\
#                                     sent_time = timezone.now())
#                 print i.user_name ,"通过审核。"
#                 send_Short_Message(i.bind_phone,"恭喜您已审核通过成为天龙健康会员，你的注册号：%s，推荐会员可以获得公司推广奖励，详见奖励模式请登录www.tljk518.com.回复TD退订【天龙健康】"%(i.user_name))
#                 #如果没有上级推荐人 不产生推荐奖
#                 if i.reference_id == 0:
#                     print "没有任何奖"
#                     return True
#                 elif i.reference_id != 0:
#                     print "有奖项发生"
#                     #如果上级为已审核就把它变成已激活
#                     up = Member.objects.filter(user_id = i.reference_id).get()
#                     if up.status.status_id == "2":
#                         up.status = MemberStatus(id = 3,status_id = '3')
#                         up.save()            
#                         Message.objects.create(user_id = up.user_id,message_title="您的帐号已激活",\
#                                    message_content=up.user_name+"您已经进入公司公排系统，感谢您对我们的支持",message_status = 0,\
#                                    sent_time = timezone.now())
#                         print up.user_id,"已经被激活"
#                     #有上级时判断 是否为 已审核 其他都不需要让上级加入公排系统因为没有订单
#                     #加入公排系统方式为将其订单加入有效时间 防止重复
#                     #o 为上级最新的订单 因为之前旧的订单可能已经有效            
#                     countOfRef = OrderForm.objects.order_by("-order_created").\
#                                  filter(user_id = Member(user_id = i.reference_id),\
#                                         service_id = service_id_,order_valid_time__isnull=True).count()
#                     if countOfRef == 0:
#                         print "上级无无效订单 不需要帮他进入公排系统，也不会有之后的广告费产生!"
#                     else:
#                         o = OrderForm.objects.order_by("-order_created").\
#                             filter(user_id = Member(user_id = i.reference_id),service_id = service_id_,order_valid_time__isnull=True)[0]
#                         o.order_valid_time = timezone.now()
#                         print "订单",o.order_id,"时间变为",o.order_valid_time
#                         o.save()
#                         #此时再对队列中进行排序
#                         list = OrderForm.objects.filter(service_id = service_id_).order_by("order_valid_time").\
#                             exclude(order_valid_time__isnull=True).all()
#                         index = 0
#                         for ob in list:
#                             if ob.order_id == o.order_id:
#                                 break
#                             else:
#                                 index = index + 1
#                         #队列 从0开始 
#                         if(index+1)/2 > 0:
#                             print list[(index-1)/2].user_id.user_id,"拿380广告费"
#                             CommissionOrder.objects.create(user_id = list[(index-1)/2].user_id,commission_price = 400*(1-tax),\
#                                                        commission_created = timezone.now(),commission_status = '0',\
#                                                        commission_type = CommissionDetail(commission_type = '3'),service_id = list[(index-1)/2].user_id.service_id)
#                             if(index %2 == 0):
#                                 print list[(index-1)/2].user_id.user_id,"发送短信 第一层拿满了"
#                                 pass
#                         if (index+1)/4 > 0:
#                             print list[(index-3)/4].user_id.user_id,"拿190广告费"
#                             CommissionOrder.objects.create(user_id = list[(index-3)/4].user_id,commission_price = 200*(1-tax),\
#                                                        commission_created = timezone.now(),commission_status = '0',\
#                                                        commission_type = CommissionDetail(commission_type = '3'),service_id = list[(index-3)/4].user_id.service_id)
#                             if((index + 2)%4 == 0):
#                                 print "发送短信 第二层拿满了"
#                                 #把爷爷变成出局了
#                                 mb = Member.objects.filter(user_id = list[(index-3)/4].user_id.user_id).get() 
#                                 mb.status = MemberStatus(id = 4,status_id = 4)
#                                 mb.save()
#                     #以上广告费结束   
#                     #开始网络推荐奖
#                     #上级先添加网络推荐奖
#                     CommissionOrder.objects.create(user_id = Member(user_id = i.reference_id),commission_price = 200*FirstRatio,\
#                                             commission_created = timezone.now(),commission_status = '0',\
#                                             commission_type = CommissionDetail(commission_type = '4'),service_id = i.service_id)     
#                     print i.reference_id,"拿到10元 网络推荐奖"
#                     #上级的上级添加网络推荐奖
#                     j = Member.objects.filter(user_id = i.reference_id).get()
#                     if j.reference_id != 0:
#                         CommissionOrder.objects.create(user_id = Member(user_id = j.reference_id),commission_price = 200*SecondRatio,\
#                                             commission_created = timezone.now(),commission_status = '0',\
#                                             commission_type = CommissionDetail(commission_type = '4'),service_id = j.service_id) 
#                         print j.reference_id,"拿到6元 网络推荐奖"
#                         #上级的上级的上级网络推荐奖
#                         k = Member.objects.filter(user_id = j.reference_id).get()
#                         if k.reference_id != 0:
#                             CommissionOrder.objects.create(user_id = Member(user_id = k.reference_id),commission_price = 200*ThirdRatio,\
#                                             commission_created = timezone.now(),commission_status = '0',\
#                                             commission_type = CommissionDetail(commission_type = '4'),service_id = k.service_id)   
#                             print k.reference_id,"拿到4元 网络推荐奖"
#                             #网络推荐奖结束开始直推荐奖励
#                             #判断当月上级推荐人已经推荐几个 0~9为200元 10~19 300元 20及以上400元
#                 args = {}
#                 arg ={}
#                 #当月订单
#                 time = timezone.now()
#                 time_1 = datetime.datetime(time.year,time.month,1)
#                 args['commission_created__gt'] = time
#                 arg['commission_created__gt'] =  time_1
#                 count = CommissionOrder.objects.filter(user_id = Member(user_id = i.reference_id))\
#                         .filter(Q(commission_type = CommissionDetail(commission_type = '0'))|\
#                         Q(commission_type = CommissionDetail(commission_type = '1'))|\
#                         Q(commission_type = CommissionDetail(commission_type = '2'))).\
#                         filter(**arg).exclude(**args).count()
#                 if count >19:
#                     print i.reference_id,"获得380元超级推荐奖"
#                     CommissionOrder.objects.create(user_id = Member(user_id = i.reference_id),commission_price = 400*(1-tax),\
#                                             commission_created = timezone.now(),commission_status = '0',\
#                                             commission_type = CommissionDetail(commission_type = '2'),service_id = i.service_id)
#                 elif count > 9:
#                     print i.reference_id,"获得285优秀推荐奖"
#                     CommissionOrder.objects.create(user_id = Member(user_id = i.reference_id),commission_price = 300*(1-tax),\
#                                             commission_created = timezone.now(),commission_status = '0',\
#                                             commission_type = CommissionDetail(commission_type = '1'),service_id = i.service)
#                 else:
#                     print i.reference_id,"获得190元推荐奖"
#                     CommissionOrder.objects.create(user_id = Member(user_id = i.reference_id),commission_price = 200*(1-tax),\
#                                             commission_created = timezone.now(),commission_status = '0',\
#                                             commission_type = CommissionDetail(commission_type = '0'),service_id = i.service)    
#                 return True
#             else:
#                 print "该会员状态不是申请加单或未审核，不能被审核"
#         except BaseException,e:
#             print e
#             return False

    #三叉树版本的审核会员
    def confirmMember(self,user_id_,service_id_):
         try:
             i = Member.objects.filter(user_id = user_id_).get()
             #不是未审核或申请加单就无法被审核
             #若是未审核变成已审核
             #若是已出局变为已激活
             if i.status.status_id == "1" or i.status.status_id == "7":
                 if i.status.status_id == "1":  
                     i.status = MemberStatus(id = 2,status_id = '2')
                     i.confirm_time = timezone.now()
                     i.save()
                     Message.objects.create(user_id = user_id_,message_title="您的帐号通过审核",\
                                            message_content=i.user_name+"您已经通过审核推荐一个人就能进入公司公排系统，感谢您对我们的支持",message_status = 0,\
                                            sent_time = timezone.now())
                     #如果为首次加单 且上级不为空判断此单为上级的第几单
                     if i.reference_id != 0:
                        #查询最近三十天上级的推荐奖类订单数量 time_1比time小30天
                        time = timezone.now()
                        #z最近30天版本
#                         time_1 = timezone.now()-datetime.timedelta(days=30)
                        time_1 = datetime.datetime(time.year,time.month,1)
                        args={}
                        arg={}
                        args['commission_created__gt'] = time
                        arg['commission_created__gt'] =  time_1
                        count = CommissionOrder.objects.filter(user_id = Member(user_id = i.reference_id))\
                            .filter(Q(commission_type = CommissionDetail(commission_type = '0'))|\
                                    Q(commission_type = CommissionDetail(commission_type = '1'))|\
                                    Q(commission_type = CommissionDetail(commission_type = '2'))|\
                                    Q(commission_type = CommissionDetail(commission_type = '6'))).\
                                    filter(**arg).exclude(**args).count()
                        if count < 2:
                            print i.reference_id,'获得190元推荐奖'
                            CommissionOrder.objects.create(user_id = Member(user_id = i.reference_id),commission_price = 200*(1-tax),\
                                                        commission_created = timezone.now(),commission_status = '0',\
                                                        commission_type = CommissionDetail(commission_type = '0'),service_id = i.service_id)
                            Message.objects.create(user_id = i.reference_id,message_title="获得推荐奖",\
                                            message_content="您已经获得190元推荐奖",message_status = 0,\
                                            sent_time = timezone.now())
                        elif count == 2:
                            print i.reference_id,'获得475元推荐奖'
                            CommissionOrder.objects.create(user_id = Member(user_id = i.reference_id),commission_price = 500*(1-tax),\
                                                        commission_created = timezone.now(),commission_status = '0',\
                                                        commission_type = CommissionDetail(commission_type = '0'),service_id = i.service_id)
                            Message.objects.create(user_id = i.reference_id,message_title="获得推荐奖,第三单另奖200元",\
                                            message_content="您已经获得475元推荐奖",message_status = 0,\
                                            sent_time = timezone.now())
                        elif count < 19:
                            print i.reference_id,'获得285元优秀推荐奖'
                            CommissionOrder.objects.create(user_id = Member(user_id = i.reference_id),commission_price = 300*(1-tax),\
                                                        commission_created = timezone.now(),commission_status = '0',\
                                                        commission_type = CommissionDetail(commission_type = '1'),service_id = i.service_id)
                            Message.objects.create(user_id = i.reference_id,message_title="获得优秀推荐奖",\
                                            message_content="您已经获得285元推荐奖",message_status = 0,\
                                            sent_time = timezone.now())
                        else:
                            print i.reference_id,'获得380元超级推荐奖'
                            CommissionOrder.objects.create(user_id = Member(user_id = i.reference_id),commission_price = 400*(1-tax),\
                                                        commission_created = timezone.now(),commission_status = '0',\
                                                        commission_type = CommissionDetail(commission_type = '2'),service_id = i.service_id)
                            Message.objects.create(user_id = i.reference_id,message_title="获得超级推荐奖",\
                                            message_content="您已经获得380元推荐奖",message_status = 0,\
                                            sent_time = timezone.now())
                        ##首次消费
                        #获取他父亲最新的订单理论上说一个人只有可能一个为确认订单
                        count = OrderForm.objects.order_by("-order_created").filter(user_id = Member(user_id = i.reference_id),\
                                                                        service_id = service_id_,order_valid_time__isnull=True).count()
                        if count == 0:
                            print "虽然推荐但是父亲没有新的订单所以没有后面的奖"
                        else:
                            o = OrderForm.objects.order_by("-order_created").filter(user_id = Member(user_id = i.reference_id),\
                                                                        service_id = service_id_,order_valid_time__isnull=True)[0]
                            o.order_valid_time = timezone.now()
                            o.save()
                            ref = Member.objects.filter(user_id = i.reference_id).get()
                            send_Short_Message(ref.bind_phone,ref.user_name+"会员您好：你已经成为vip会员，将自动进入公司系统公排模式,推荐奖不限，推荐越多奖金越多。咨询电话：0575-87755511.回复TD退订【天龙健康】")
                            #此时再对队列中进行排序
                            list = OrderForm.objects.filter(service_id = service_id_).order_by("order_valid_time").\
                                     exclude(order_valid_time__isnull=True).all()
                            index = 0
                            for ob in list:
                                if ob.order_id == o.order_id:
                                    break
                                else:
                                    index = index + 1
                            #队列从0开始 
                            if(index+2)/3 > 0:
                                print list[(index-1)/3].user_id.user_id,"拿285广告费"
                                CommissionOrder.objects.create(user_id = list[(index-1)/3].user_id,commission_price = 300*(1-tax),\
                                                        commission_created = timezone.now(),commission_status = '0',\
                                                        commission_type = CommissionDetail(commission_type = '3'),service_id = list[(index-1)/3].user_id.service_id)
                                Message.objects.create(user_id = list[(index-1)/3].user_id.user_id,message_title="获得第一层广告费285元",\
                                            message_content="您已经获得285元广告费",message_status = 0,\
                                            sent_time = timezone.now())
                                if(index %3 == 0):
                                    print list[(index-1)/3].user_id.user_id,"发送短信 第一层拿满了"
                            if(index+5)/9 > 0:
                                print list[(index-4)/9].user_id.user_id,"拿95广告费"
                                CommissionOrder.objects.create(user_id = list[(index-4)/9].user_id,commission_price = 100*(1-tax),\
                                                        commission_created = timezone.now(),commission_status = '0',\
                                                        commission_type = CommissionDetail(commission_type = '3'),service_id = list[(index-4)/9].user_id.service_id)
                                Message.objects.create(user_id = list[(index-4)/9].user_id.user_id,message_title="获得第二层广告费95元",\
                                            message_content="您已经获得第二层广告费95元",message_status = 0,\
                                            sent_time = timezone.now())
                                if((index + 6)%9 == 0):
                                    print "发送短信 第二层拿满了"
                                    send_Short_Message(list[(index-4)/9].user_id.bind_phone,"会员您好：您的VIP编号："+list[(index-4)/9].user_id.user_name+"已成为公司高级会员，享受公司特别优惠政策，只需继续加单800元，就可以再次直接生成VIP会员，重新获取产品又可获得自动公排广告奖励。咨询电话：0575-87755511.回复TD退订【天龙健康】")
                                    #把爷爷变成出局了
                                    mb = Member.objects.filter(user_id = list[(index-4)/9].user_id.user_id).get() 
                                    mb.status = MemberStatus(id = 4,status_id = 4)
                                    mb.save()             
                     else:
                         print "没有上级不产生推荐奖其他奖"
                         return
                ##复销情况
                 elif i.status.status_id == "7":
                     i.status = MemberStatus(id = 3,status_id = '3')
                     i.confirm_time = timezone.now()
                     i.save()
                     Message.objects.create(user_id = user_id_,message_title="您的帐号已经激活",\
                                            message_content=i.user_name+"您已经进入公司公排系统，感谢您对我们的支持",message_status = 0,\
                                            sent_time = timezone.now())
                     send_Short_Message(i.bind_phone,i.user_name+"会员您好：你已经成为vip会员，将自动进入公司系统公排模式,推荐奖不限，推荐越多奖金越多。咨询电话：0575-87755511.回复TD退订【天龙健康】")
                     print "已激活"
                     #先将自己的订单变为有效
                     o = OrderForm.objects.order_by("-order_created").filter(user_id = Member(user_id = user_id_),\
                                                                        service_id = service_id_,order_valid_time__isnull=True)[0]
                     o.order_valid_time = timezone.now()
                     o.save()
                     print o.order_id,"已经变成有效了" 
                     list = OrderForm.objects.filter(service_id = service_id_).order_by("order_valid_time").\
                                     exclude(order_valid_time__isnull=True).all()
                     index = 0
                     for ob in list:
                         if ob.order_id == o.order_id:
                             break
                         else:
                             index = index + 1
            
                    #队列 从0开始 
                     if(index+2)/3 > 0:
                         print list[(index-1)/3].user_id.user_id,"拿285广告费"
                         CommissionOrder.objects.create(user_id = list[(index-1)/3].user_id,commission_price = 300*(1-tax),\
                                                        commission_created = timezone.now(),commission_status = '0',\
                                                        commission_type = CommissionDetail(commission_type = '3'),service_id = list[(index-1)/3].user_id.service_id)
                         Message.objects.create(user_id = list[(index-1)/3].user_id.user_id,message_title="获得第一层广告费285元",\
                                            message_content="您已经获得285元广告费",message_status = 0,\
                                            sent_time = timezone.now())
                         if(index %3 == 0):
                             print list[(index-1)/3].user_id.user_id,"发送短信 第一层拿满了"
                     if(index+5)/9 > 0:
                         print list[(index-4)/9].user_id.user_id,"拿95广告费"
                         CommissionOrder.objects.create(user_id = list[(index-4)/9].user_id,commission_price = 100*(1-tax),\
                                                        commission_created = timezone.now(),commission_status = '0',\
                                                        commission_type = CommissionDetail(commission_type = '3'),service_id = list[(index-4)/9].user_id.service_id)
                         Message.objects.create(user_id = list[(index-4)/9].user_id.user_id,message_title="获得第二层广告费95元",\
                                            message_content="您已经获得第二层广告费95元",message_status = 0,\
                                            sent_time = timezone.now())
                         if((index + 6)%9 == 0):
                             print "发送短信 第二层拿满了"
                            #把爷爷变成出局了
                             mb = Member.objects.filter(user_id = list[(index-4)/9].user_id.user_id).get() 
                             mb.status = MemberStatus(id = 4,status_id = 4)
                             mb.save()
                             send_Short_Message(list[(index-4)/9].user_id.bind_phone,"会员您好：您的VIP编号："+list[(index-4)/9].user_id.user_name+"已成为公司高级会员，享受公司特别优惠政策，只需继续加单800元，就可以再次直接生成VIP会员，重新获取产品又可获得自动公排广告奖励。咨询电话：0575-87755511.回复TD退订【天龙健康】")
                     if i.reference_id != 0:
                         print i.reference_id,'获得190元复投推荐奖'
                         CommissionOrder.objects.create(user_id = Member(user_id = i.reference_id),commission_price = 200*(1-tax),\
                                                        commission_created = timezone.now(),commission_status = '0',\
                                                        commission_type = CommissionDetail(commission_type = '6'),service_id = i.service_id)
                         Message.objects.create(user_id = i.reference_id,message_title="获得复投推荐奖",\
                                            message_content="您已经获得190元复投推荐奖",message_status = 0,\
                                            sent_time = timezone.now())
                     else:
                         print "没有上级不产生复投推荐奖"
                         return                              
             else:
                print "该会员状态不是申请加单或未审核，不能被审核"
         except BaseException,e:
                print e
                return False
    
    #我直接推荐的会员(可用于我的推荐网络)
    def myReference(self,user_id_,pageNum=1):
        startPos = (pageNum-1)*ONE_PAGE_OF_DATA
        endPos = pageNum*ONE_PAGE_OF_DATA
        try:
            myReferenceList = Member.objects.filter(reference_id = user_id_ ).all()[startPos:endPos]
            count = Member.objects.filter(reference_id = user_id_ ).count()
            if count%ONE_PAGE_OF_DATA == 0:
                return myReferenceList,(count/ONE_PAGE_OF_DATA),count
            else :
                return myReferenceList,(count/ONE_PAGE_OF_DATA)+1,count
        except BaseException,e:
            print e
    #获取用户Id
    @staticmethod 
    def GetUser(username_):
        try :
            user = Member.objects.filter(user_name = username_).get()
            return user
        except BaseException,e:
            print e
    def getUser(self,username_):
        try :
            user = Member.objects.filter(user_name = username_).get()
            return user
        except BaseException,e:
            print e
    #我间接推荐的会员
    def myIndirectRef(self,user_id_,pageNum=1):
        startPos = (pageNum-1)*ONE_PAGE_OF_DATA
        endPos = pageNum*ONE_PAGE_OF_DATA
        try:
            resultlist = []
            count = 0
            #孩子
            reflist_0 = Member.objects.filter(reference_id = user_id_ ).all()
#             count = Member.objects.filter(reference_id = user_id_ ).count()
            if reflist_0 !=None:
                #孙子
                for i in reflist_0:
                    #不把直接推荐的放进去
#                     resultlist.append(i)
                    reflist_1 = Member.objects.filter(reference_id = i.user_id ).all()
                    count = count + Member.objects.filter(reference_id = i.user_id ).count()
                    if reflist_1 !=None:
                        #曾孙
                        for i1 in reflist_1:
                            resultlist.append(i1)
                            reflist_2 = Member.objects.filter(reference_id = i1.user_id ).all()
                            count = count + Member.objects.filter(reference_id = i1.user_id ).count()
                            if reflist_2 !=None:
                                for i2 in reflist_2:
                                    resultlist.append(i2)
            if count%ONE_PAGE_OF_DATA == 0:
                return resultlist[startPos:endPos],(count/ONE_PAGE_OF_DATA),count
            else :
                return resultlist[startPos:endPos],(count/ONE_PAGE_OF_DATA)+1,count                
        except BaseException,e:
            print e
    #会员网络不需要分页全部显示
    #role = 0 为服务中心，= 1为会员默认为第一页
    def myMemberNet(self,userOrServiceid_,role_,pageNum=1):
        try:
            if role_ == '0':
                memberlist = Member.objects.filter(reference_id = 0,service_id = userOrServiceid_).all()
                return memberlist
            if role_ == '1':
                memberlist = Member.objects.filter(reference_id = userOrServiceid_).all()
                return memberlist
        except BaseException,e:
            print e
            
    #service_id 查出对应服务点的会员信息
    #user_or_phone_用户名或手机号
    #member_status_ 1:未审核 2：已审核 3：已激活 4:已出局 5：服务中心锁定6：管理员锁定 7：申请加单
    #time_order_ 0:注册时间倒序 1:注册时间正序 2:确认时间倒序 3:确认时间正序
    #reg_way 0:所有注册点 1:服务中心注册 2.会员推荐
    
    def MemberList(self,service_id_,user_or_phone_=None,member_status_=None,time_order_='0',reg_way='0',\
                   reg_start_time_=None,reg_end_time_=None,conf_start_time_=None,conf_end_time_=None,pageNum=1):
        startPos = (pageNum-1)*ONE_PAGE_OF_DATA
        endPos = pageNum*ONE_PAGE_OF_DATA
        args= {}
        arg={}
        i = []
        count = 0
        orderlist = {'0':'-register_time','1':'register_time','2':'-confirm_time','3':'confirm_time'}
        if member_status_ !=None:
            args['status'] = MemberStatus(id = int(member_status_) ,status_id = member_status_)
            #args['status_id'] = member_status_
        if reg_start_time_ !=None:
            args['register_time__gt']=reg_start_time_
        if conf_start_time_ !=None:
            args['confirm_time__gt']=conf_start_time_
        if reg_end_time_ !=None:
            arg['register_time__gt']=reg_end_time_
        if conf_end_time_ !=None:
            arg['confirm_time__gt']=conf_end_time_
        
        if reg_way =='0':
            if user_or_phone_ != None:
                i = Member.objects.filter(Q(user_name = user_or_phone_)|Q(bind_phone=user_or_phone_))\
                .filter(service_id = service_id_).filter(**args).exclude(**arg)\
                    .order_by(orderlist.get(time_order_)).all()[startPos:endPos]
                count = Member.objects.filter(Q(user_name = user_or_phone_)|Q(bind_phone=user_or_phone_)).\
                filter(service_id = service_id_).filter(**args).exclude(**arg)\
                    .order_by(orderlist.get(time_order_)).count()
            elif user_or_phone_ == None:
                i = Member.objects.filter(service_id = service_id_).filter(**args).exclude(**arg).\
                order_by(orderlist.get(time_order_)).all()[startPos:endPos]
                count = Member.objects.filter(service_id = service_id_).filter(**args).exclude(**arg).\
                order_by(orderlist.get(time_order_)).count()
        elif reg_way =='1':
            if user_or_phone_ != None:
                i = Member.objects.filter(Q(user_name = user_or_phone_)|Q(bind_phone=user_or_phone_)).\
                filter(service_id = service_id_,reference_id = '0').filter(**args).exclude(**arg)\
                    .order_by(orderlist.get(time_order_)).all()[startPos:endPos]
                count = Member.objects.filter(Q(user_name = user_or_phone_)|Q(bind_phone=user_or_phone_)).\
                filter(service_id = service_id_,reference_id = '0').filter(**args).exclude(**arg)\
                    .order_by(orderlist.get(time_order_)).count()
            elif user_or_phone_ == None:
                i = Member.objects.filter(service_id = service_id_,reference_id = '0').filter(**args).\
                exclude(**arg).order_by(orderlist.get(time_order_)).all()[startPos:endPos]
                count = Member.objects.filter(service_id = service_id_,reference_id = '0').filter(**args).\
                exclude(**arg).order_by(orderlist.get(time_order_)).count()
        if count%ONE_PAGE_OF_DATA == 0:
            return i,(count/ONE_PAGE_OF_DATA),count
        else:
            return i,(count/ONE_PAGE_OF_DATA)+1,count
    #查看会员信息
    def myInfo(self,user_id_):
        try:
            return Member.objects.filter(user_id = user_id_).get()
        except BaseException,e:
            print e
    #修改会员资料 可修改有 密码，绑定手机号，微信号，开户银行,账户,持卡人,收货人,收货电话,收货地址
    def fixInfo(self,user_id_,pwd_=None,bind_phone_=None,weixinId_=None,bank_=None,account_=None,card_holder_=None,\
                receiver_=None,receiver_phone_=None,receiver_addr_=None,member_status_ =None):
        try :
            i = Member.objects.filter(user_id = user_id_).get()
            if pwd_ !=None:
                #需要换成MD5的hash值
                i.password = pwd_
            if bind_phone_ !=None:
                i.bind_phone = bind_phone_
            if weixinId_ !=None:
                i.weixin_id =weixinId_
            if bank_ !=None:
                i.bank = bank_
            if account_ != None:
                i.account = account_
            if card_holder_ !=None:
                i.card_holder = card_holder_
            if receiver_ !=None:
                i.receiver = receiver_
            if receiver_phone_ !=None:
                i.receiver_phone = receiver_phone_
            if receiver_addr_ !=None:
                i.receiver_addr = receiver_addr_
            if member_status_!=None:
                i.status = MemberStatus(id = member_status_,status_id = member_status_)
            i.save()
            return True
        except BaseException,e:
            print e
            return False
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

    def getAllMsg(self):
      msgs =Message.objects.all()
      return msgs

    def getFilterMsg(self,msgid):
      msg = Message.objects.filter(message_id = msgid).get()
      return msg

    #该函数只是改变了消息的状态 服务中心或用户阅读了该消息
    def readMessage(self,message_id_):
        try:
            msg = Message.objects.filter(message_id = message_id_).get()
            msg.message_status = 1
            msg.save()
            return True
        except BaseException,e:
            print e
            return False
    #message_status_ 为2表示所有消息 0表示未读，1表示为已读 role = 0 为会员,= 1为服务中心
    def myMessage(self,id_,role_,message_status_ = "2",pageNum = 1):
        try:
            startPos = (pageNum-1)*ONE_PAGE_OF_DATA
            endPos = pageNum*ONE_PAGE_OF_DATA
            if role_ == "0":
                if message_status_ == "2":
                    msglist = Message.objects.filter(user_id = id_).all()[startPos:endPos]
                    count = Message.objects.filter(user_id = id_).count()
                    if count%ONE_PAGE_OF_DATA == 0:
                        return msglist,(count/ONE_PAGE_OF_DATA),count
                    else :
                        return msglist,(count/ONE_PAGE_OF_DATA)+1,count
                else:
                    msglist = Message.objects.filter(user_id = id_,message_status = message_status_).all()[startPos:endPos]
                    count = Message.objects.filter(user_id = id_,message_status = message_status_).count()
                    if count%ONE_PAGE_OF_DATA == 0:
                        return msglist,(count/ONE_PAGE_OF_DATA),count
                    else :
                        return msglist,(count/ONE_PAGE_OF_DATA)+1,count
            elif role_ == "1":
                if message_status_ == "2":
                    msglist = Message.objects.filter(service_id = id_).all()[startPos:endPos]
                    count = Message.objects.filter(service_id = id_).count()
                    if count%ONE_PAGE_OF_DATA == 0:
                        return msglist,(count/ONE_PAGE_OF_DATA),count
                    else :
                        return msglist,(count/ONE_PAGE_OF_DATA)+1,count
                else:
                    msglist = Message.objects.filter(service_id = id_,message_status = message_status_).all()[startPos:endPos]
                    count = Message.objects.filter(service_id = id_,message_status = message_status_).count()
                    if count%ONE_PAGE_OF_DATA == 0:
                        return msglist,(count/ONE_PAGE_OF_DATA),count
                    else :
                        return msglist,(count/ONE_PAGE_OF_DATA)+1,count
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
    #审核的时间戳 用于佣金树排序
    order_finished = models.DateTimeField(blank=True, null=True)
    order_memo = models.CharField(max_length=100, blank=True, null=True)
    order_status = models.CharField(max_length=5, blank=True, null=True)
    express_name = models.CharField(max_length=20, blank=True, null=True)
    express_number = models.CharField(max_length=50, blank=True, null=True)
    #只用于加单因为 首次下单 在注册时下单
    def createOrder(self,service_id_,user_id_,order_price_,order_type_,order_memo_,order_status_="未发货"):
        try:
            i = Member.objects.filter(user_id = user_id_).get()
            i.status = MemberStatus(id = 7,status_id = 7)
            i.save()
            Message.objects.create(service_id = service_id_,message_title=i.user_name+"申请加单，请审核",\
                                   message_content=i.user_name+"申请加单，请至订单列表进行审核。",message_status = 0,\
                                   sent_time = timezone.now())
            OrderForm.objects.create(service_id = service_id_,user_id = Member(user_id = user_id_),order_price = order_price_,\
                                 order_type = order_type_,order_created = timezone.now(),order_memo = order_memo_,\
                                 order_status =order_status_)
            print user_id_,"加单成功",timezone.now()
            ref = Member.objects.filter(user_id = i.user_id).get()
            send_Short_Message(ref.bind_phone,ref.user_name+"会员您好:由您推荐的会员"+i.user_name+" 再次加单成功，你将获得推荐奖，自动扣税5%。咨询电话：0575-87755511.回复TD退订【天龙健康】")
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
    #服务中心订单以及会员界面中订单 #order_type 为0表示未发货的,1表示已发货的，2为所有
    #若不提供user_or_phone_ 返回一个list 用一个循环取读
    #若提供user_or_phone_ 返回一个list,list中的元素也为list 因为多个用户可能同时为一个手机号
    def myMemberOrder(self,user_id_=None,service_id_=None,user_or_phone_=None,order_type_='2',start_time_=None,end_time_=None,pageNum=1):
        startPos = (pageNum-1)*ONE_PAGE_OF_DATA
        endPos = pageNum*ONE_PAGE_OF_DATA
        try:
            arg={}
            args={}
            count = 0
            orderlist = []
            money = 0
            if user_id_!=None:
                args['user_id']=user_id_
            if service_id_ !=None:
                args['service_id']=service_id_
            if start_time_ !=None:
                args['order_created__gt']=start_time_
            if order_type_ == "0":
                args['order_status']='未发货'
            if order_type_ == "1":
                args['order_status']='已发货'
            
            if end_time_ !=None:
                arg['order_created__gt']=end_time_
                #如果用户名或者绑定手机号给出
                if user_or_phone_ !=None:
                    users = Member.objects.filter(Q(user_name = user_or_phone_)|Q(bind_phone=user_or_phone_)).all()
                    for i in users:
                        orderlist.append(OrderForm.objects.filter(**args).filter(user_id = i.user_id).exclude(**arg).all())
                        count = count + OrderForm.objects.filter(**args).filter(user_id = i.user_id).exclude(**arg).count()
                    for j in orderlist:
                        money = money +j.order_price
                elif user_or_phone_ ==None:
                    orderlist = OrderForm.objects.filter(**args).exclude(**arg).all()[startPos:endPos]
                    count = OrderForm.objects.filter(**args).exclude(**arg).count()
                    for j in orderlist:
                        money = money +j.order_price
            elif end_time_ == None:
                #如果用户名或者绑定手机号给出
                if user_or_phone_ !=None:
                    users = Member.objects.filter(Q(user_name = user_or_phone_)|Q(bind_phone=user_or_phone_)).all()
                    for i in users:
                        orderlist.append(OrderForm.objects.filter(**args).filter(user_id = i.user_id).all())
                        count = count + OrderForm.objects.filter(**args).filter(user_id = i.user_id).count()
                    for j in orderlist:
                        money = money +j.order_price
                elif user_or_phone_ ==None:
                        orderlist = OrderForm.objects.filter(**args).all()[startPos:endPos]
                        count = OrderForm.objects.filter(**args).count()
                        for j in orderlist:
                            money = money +j.order_price
            if count%ONE_PAGE_OF_DATA == 0 and user_or_phone_==None:
                return orderlist,(count/ONE_PAGE_OF_DATA),count,money
            elif count%ONE_PAGE_OF_DATA != 0 and user_or_phone_==None:
                return orderlist,(count/ONE_PAGE_OF_DATA)+1,count,money    
            elif count%ONE_PAGE_OF_DATA == 0 and user_or_phone_!=None:
                return orderlist[startPos:endPos],(count/ONE_PAGE_OF_DATA),count,money
            elif count%ONE_PAGE_OF_DATA != 0 and user_or_phone_!=None:
                return orderlist[startPos:endPos],(count/ONE_PAGE_OF_DATA)+1,count,money
        except BaseException,e:
            print e

    def myDeliverInfoByOrderId(self,order_id_):
        orderinfo_by_orderid = OrderForm.objects.filter(order_id = order_id_).get()
        return orderinfo_by_orderid

class Product(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_price = models.FloatField(blank=True, null=True)
 
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=20)
    service_pwd = models.CharField(max_length=32, blank=True, null=True)
    service_area = models.CharField(max_length=20, blank=True, null=True)
    #上级服务中心 只有副中心才有
    service_ref = models.BigIntegerField(blank=True, null=True)
    #副中心负责人
    service_response = models.CharField(max_length=20, blank=True, null=True)
    #服务(副)中心备注
    service_memo = models.CharField(max_length=200, blank=True, null=True)
    #role 为1 表示服务点，2表示已经启用的副中心，3表示未启用的副中心
    role = models.CharField(max_length=1, blank=True, null=True)
    def fixServicePwd(self,service_id_,old_pwd,new_pwd):
        try:
            serviceEntity = Service.objects.filter(service_id = service_id_).get()
            if serviceEntity.password == old_pwd:
                serviceEntity.password = new_pwd
                serviceEntity.save()
                return True
            else:
                return False
        except BaseException,e:
            print e
    #副中心保存(密码未做)
    def saveSecService(self,service_name_,service_pwd_,service_role_=None,service_area_=None,\
                       service_ref_=None,service_response_=None,service_memo_=None):
        i = None
        try:
            i = Service.objects.filter(service_ref = service_ref_)
            if not i:
                Service.objects.create(service_name = service_name_,service_pwd = service_pwd_,role = service_role_,\
                                       service_area = service_area_,service_ref = service_ref_,service_response = service_response_,\
                                       service_memo = service_memo_)
            if i:
                y = i.get()
                y.service_name = service_name_
                y.service_pwd = service_pwd_
                y.role = service_role_
                y.service_area = service_area_
                y.service_ref = service_ref_
                y.service_response = service_response_
                y.service_memo = service_memo_
                y.save()
        except BaseException,e:
            print e
    #获取副中心
    def getSecService(self,service_id_):
        try:
            return Service.objects.filter(service_ref = service_id_).get()
        except BaseException,e:
            print e
            return False
            #获取用户Id
    @staticmethod 
    def GetService(service_name_):
        try :
            service = Service.objects.filter(service_name = service_name_).get()
            return service
        except BaseException,e:
            print e
class ServiceAccount(models.Model):
    service = models.ForeignKey(Service, models.DO_NOTHING)
    bank = models.CharField(primary_key=True, max_length=255)
    bank_account = models.CharField(max_length=50, blank=True, null=True)
    card_holder = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    #公司收款账户    
    def comBank(self,service_id_,pageNum = 1):
        startPos = (pageNum-1)*ONE_PAGE_OF_DATA
        endPos = pageNum*ONE_PAGE_OF_DATA
        try:
            account_list = ServiceAccount.objects.filter(service = Service(service_id = service_id_)).all()[startPos:endPos]
            count = ServiceAccount.objects.filter(service = Service(service_id = service_id_)).count()
            if count%ONE_PAGE_OF_DATA == 0:
                return account_list,(count/ONE_PAGE_OF_DATA),count
            else:
                return account_list,(count/ONE_PAGE_OF_DATA)+1,count
        except BaseException,e:
            print e 
    
class ShortMessage(models.Model):
    message_id = models.IntegerField(primary_key=True)
    message_content = models.CharField(max_length=200, blank=True, null=True)

def send_Short_Message(phone,content):
#     print phone,user_name
    url = "http://sdk.shmyt.cn:8080/manyousms/sendsms?account=hztl&password=hztl2016&mobiles=%s&content=%s"%(phone,content)
    print url    
#     res_data = urllib2.urlopen(url)
#     res = json.loads(res_data.read())
#     a = res['codetype']
#     if int(a) == 0:
#         print "sendsuccess"
#     else:
#         print "error"
