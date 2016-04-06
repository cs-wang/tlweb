# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from db import models
import json
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import pytz
# Create your views here.

def DashBoard(request):
	context = {}
	return render(request, 'Services/DashBoard.html', context)

def NoticeList(request):
	context = {}
	return render(request, 'Services/NoticeList.html', context)

def MsgList(request):
	sta = request.GET.get('sta')
	if sta==None:
		sta="2"
	msgobj = models.Message()
	msgs = msgobj.myMessage(1, 1, sta)
	context = { 'msglist':msgs,
				'msgnum':len(msgs), }
#	msgobj = models.Message()
# 	msgobj.readMessage(5)

 	msglist,pageMax =  msgobj.myMessage(1,"1","2",3)
 	for i in msglist:
 		print i.message_id
 	print "最多可以有" ,pageMax

# 	msgobj.myMessage(1,1,0)
	return render(request, 'Services/MsgList.html', context)

def ViewMsg(request):
	msgid = request.GET.get('MsgId')
	msg_ = models.Message()
	msg = msg_.getFilterMsg(msgid)
	context = {	'msgtitle':msg.message_title,
				'msgcontent':msg.message_content,
				'msgid':msg.message_id, }
	return render(request, 'Services/ViewMsg.html', context)

def MsgRead(request):
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
	context = {}
#	 if request.method == 'GET':
#		 return 
#	 elif request.method == 'POST':
#		 return

# 	member_ = models.Member()
# 	flag = member_.register('zdg',"赵镇辉啊","delegation_phone_","delegation_info_",\
# 		  "bind_phone_","pwd","weixinId","bank_","account_","cardHolder","receiver_","reciever_phone_",\
# 		  "receiver_addr_","order_Memo",1,0)   
	return render(request, 'Services/MemberEdit.html', context)

def MemberList(request):
	member_ = models.Member()
	memberlist = member_.MemberList()
	print "MemberList:",memberlist
	context = { 'memberlist':memberlist, }
	flag = member_.activateMember(3,1)
	return render(request, 'Services/MemberList.html', context)

def SetAudit(request):
	context = {}
	return render(request, 'Services/SetAudit.html', context)

def MemberOrder(request):
	context = {}
	naive = parse_datetime("2017-02-21 10:28:45")
 	naive1 = parse_datetime("2016-04-01 10:28:45")
 	time_ = pytz.timezone("UTC").localize(naive, is_dst=None)
 	time_1 = pytz.timezone("UTC").localize(naive1, is_dst=None)	
	order_ = models.OrderForm()
	order_list,maxPage = order_.myServiceOrder(1,"123",'2',time_1,time_)
	for i in order_list:
		print i.order_id
	print "最多", maxPage
#  	order_.createOrder(1,1,1000,1,"A+B都是货物啊","未发货")
#	order_.comfirmDelivery(1,"五环快递","1232131231232131231")

	
# 	print order_.myMemberOrder(1,time_1,time_,2)
	return render(request, 'Services/MemberOrder.html', context)

def UserMap(request):
	context = {}
	member_ = models.Member()
	memlist ,PageMax= member_.myMemberNet(1,'0',1)
	for i in memlist:
		print i.user_id,i.user_name
	print "最多",PageMax,"页"
	
	return render(request, 'Services/UserMap.html', context)

def ComBank(request):
	context = {}
	return render(request, 'Services/ComBank.html', context)

def Promotion(request):
	context = {}
	return render(request, 'Services/Promotion.html', context)

def AdviceList(request):

# 	context = {}
# 	advice_ = models.Advice()
# 	naive = parse_datetime("2016-03-21 10:28:45")
# 	time_ = pytz.timezone("UTC").localize(naive, is_dst=None)	
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
	advid = request.GET.get('id')
	print "advid:",advid
	advobj = models.Advice()
	adv = advobj.one_advice(advid)
	context = {'adv':adv}
	return render(request, 'Services/AdviceView.html', context)

def AdviceSub(request):
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
	context = {}
	return render(request, 'Services/SubService.html', context)
