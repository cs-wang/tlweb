# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from db import models
import datetime
import json
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import pytz
import urllib2



def DashBoard(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
# 	send_Short_Message(15757116149,"zzh")
	context = {}
	return render(request, 'Services/DashBoard.html', context)

def NoticeList(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	context = {}
	return render(request, 'Services/NoticeList.html', context)

def MsgList(request):

	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	sta = request.GET.get('sta')
	if sta==None:
		sta="2"
	msgobj = models.Message()
	msgs = msgobj.myMessage(1, 1, sta)
	context = { 'msglist':msgs,
				'msgnum':0, }
#	msgobj = models.Message()
# 	msgobj.readMessage(5)

#  	msglist,pageMax =  msgobj.myMessage(1,"1","2",3)
#  	for i in msglist:
#  		print i.message_id
#  	print "最多可以有" ,pageMax

# 	msgobj.myMessage(1,1,0)
	return render(request, 'Services/MsgList.html', context)

def ViewMsg(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	msgid = request.GET.get('MsgId')
	msg_ = models.Message()
	msg = msg_.getFilterMsg(msgid)
	context = {	'msgtitle':msg.message_title,
				'msgcontent':msg.message_content,
				'msgid':msg.message_id, }
	return render(request, 'Services/ViewMsg.html', context)

def MsgRead(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	msgid = request.POST.get('MsgId')
	msg_ = models.Message()
	msg_.readMessage(msgid)
	msg = msg_.getFilterMsg(msgid)
	print msg.message_id,msg.message_status
	if msg.message_status == "1":
		obj = {'result':'t'}
	else:
		obj = {'result':'f'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

def MemberEdit(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	context = {}
#	 if request.method == 'GET':
#		 return 
#	 elif request.method == 'POST':
#		 return

 	member_ = models.Member()
	flag = member_.register('35',"12","delegation_phone_","delegation_info_",\
		  "bind_phone_","pwd","weixinId","bank_","account_","cardHolder","receiver_","reciever_phone_",\
		  "receiver_addr_","order_Memo",1,1)   
# 	print member_.fixInfo(1,"改密码咯","新手机号码","新微信号码","新开户银行","新账户啊","新持卡人啊","新收货人啊","新收货电话啊","新收获地址啊")
	
	return render(request, 'Services/MemberEdit.html', context)

def MemberList(request):
 	member_ = models.Member()
# 	memberlist,pageMax,i = member_.MemberList(1,user_or_phone_=None,member_status_=None,time_order_='0',reg_way='0',\
#                    reg_start_time_=None,reg_end_time_=None,conf_start_time_=None,conf_end_time_="1994-04-20",pageNum=1)
#  	for i in memberlist:
#  		print i.user_name
# 	print "MemberList:",memberlist
#  	context = { 'memberlist':memberlist, }
# 	flag = member_.activateMember(3,1)
# 	list , pageMax = member_.myReference('1',1)
# 	print list.count()
	#print "最多",pageMax
	#list_1,list_2,list_3, pageMax = 
# 	list, pageMax = member_.myIndirectRef('1',1)

# 	print list
# 	print "最多",pageMax
	#print member_.myInfo(1).user_name
# 	if request.session['role'] != '1':
# 		return HttpResponseRedirect('/')

# 	memberlist,PageMax,count= member_.MemberList(1,user_or_phone_=123,member_status_=None,time_order_='0',reg_way='0',\
# 				   reg_start_time_=None,reg_end_time_=None,conf_start_time_=None,conf_end_time_=None,pageNum=1)
# 	for i in memberlist:
# 		print i.user_id
# 	print "最多",PageMax
# 	print count
# 	context = { 'memberlist':memberlist, }
	context = {}
# 	co = models.CommissionOrder() 
# 	name_list, ref_list = co.bestTenPeople(1)
# 	for i in range(0,len(name_list)):
# 		print name_list[i],ref_list[i]

# 	co.getGreatOrSuper(1)

  	flag = member_.confirmMember(35,1)
# 	print timezone.localtime(timezone.now())

	return render(request, 'Services/MemberList.html', context)

def SetAudit(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	context = {}
	return render(request, 'Services/SetAudit.html', context)

def MemberOrder(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	context = {}
 	order_ = models.OrderForm()
# 	for i in order_list:
# 		print i.order_id
# 	print "最多", maxPage
# 	order_.createOrder(1,1,800,1,"1的第2条订单","未发货")
#	order_.comfirmDelivery(1,"五环快递","1232131231232131231")

    	list,pageMax,count = order_.myMemberOrder(user_id_=1,service_id_=1,\
 							 user_or_phone_=None,order_type_='2',start_time_="2016-04-11",end_time_="2016-04-13",pageNum=1)
	for i in list:
# 		for j in i :
			print i.order_id
# 	print "最多",pageMax
# 	print "总数",count
	return render(request, 'Services/MemberOrder.html', context)

def UserMap(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	context = {}
	member_ = models.Member()
	memlist ,PageMax= member_.myMemberNet(1,'0',1)
	for i in memlist:
		print i.user_id,i.user_name
	print "最多",PageMax,"页"
	
	return render(request, 'Services/UserMap.html', context)

def ComBank(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	context = {}
	return render(request, 'Services/ComBank.html', context)

def Promotion(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	context = {}
	pro = models.CommissionOrder()
# 	list, pageMax = pro.commissionList(user_name_=None,commission_status_=None,commission_type_=None,commision_created_start_=None,commision_created_end_=None,time_order_='0',pageNum=1)
# 	for i in list :
# 		print i.commission_type.commission_desc
# 	print "最多",pageMax
# 	pro.deliverComm(1)
# 	pro.confirmComm(1)
	return render(request, 'Services/Promotion.html', context)

def AdviceList(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
# 	context = {}
# 	advice_ = models.Advice()
# 	adlist,maxPage =  advice_.my_advice(1,"0",None,None,time_,timezone.now())
# 	for i in adlist :
# 		print i.advice_id
# 	print "最多",maxPage
	advobj = models.Advice()
	advlist = advobj.my_advice(1)
	print "my_advice:",advlist
	context = {'advlist':advlist}

	return render(request, 'Services/AdviceList.html', context)

def AdviceView(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	advid = request.GET.get('id')
	print "advid:",advid
	advobj = models.Advice()
	adv = advobj.one_advice(advid)
	context = {'adv':adv}
	return render(request, 'Services/AdviceView.html', context)

def AdviceSub(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	advid = request.POST.get('id')
	advcon = request.POST.get('info')
	print "advcon:",advcon
	advobj = models.Advice()
	advobj.reply_advice(1,advcon,1,advid)
	advice = advobj.one_advice(advid)
	if advice.advice_status == "1":
		obj = {'result':'t'}
	else:
		obj = {'result':'f'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

def SubService(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	ser = models.Service()
	#ser.saveSecService("改个名字","service_pwd_",None,"service_area_",\
#                        '2',"老zhuji","老李备忘录")
	print ser.getSecService('2').service_id
	context = {}
	return render(request, 'Services/SubService.html', context)
