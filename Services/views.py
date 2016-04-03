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
	msg_ = models.Message()
	msgs = msg_.getAllMsg()
	context = {'msglist':msgs,'msgnum':len(msgs)}
#	msgobj = models.Message()
# 	msgobj.readMessage(5)
# 	msgobj.myMessage(1,1,0)
	return render(request, 'Services/MsgList.html', context)

def ViewMsg(request):
	msgid = request.GET.get('MsgId')
	msg_ = models.Message()
	msg = msg_.getFilterMsg(msgid)
	context = {'msgtitle':msg.message_title,'msgcontent':msg.message_content,'msgid':msg.message_id}
	return render(request, 'Services/ViewMsg.html', context)

def MsgRead(request):
	msgid = request.POST.get('MsgId')
	print msgid
	msg_ = models.Message()
	#msg_.updateMsgStatus(msgid)
	msg = msg_.getFilterMsg(msgid)

	print msg.message_status
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
	context = {}
	member_ = models.Member()
	flag = member_.activateMember(3,1)
	return render(request, 'Services/MemberList.html', context)

def MemberOrder(request):
	context = {}
	order_ = models.OrderForm()
 	order_.createOrder(1,1,1000,1,"A+B都是货物啊","未发货")
#	order_.comfirmDelivery(1,"五环快递","1232131231232131231")

# 	naive = parse_datetime("2017-02-21 10:28:45")
# 	naive1 = parse_datetime("2016-04-01 10:28:45")
# 	time_ = pytz.timezone("UTC").localize(naive, is_dst=None)
# 	time_1 = pytz.timezone("UTC").localize(naive1, is_dst=None)		
# 	print order_.myMemberOrder(1,time_1,time_,2)
	return render(request, 'Services/MemberOrder.html', context)

def UserMap(request):
	context = {}
	return render(request, 'Services/UserMap.html', context)

def ComBank(request):
	context = {}
	return render(request, 'Services/ComBank.html', context)

def Promotion(request):
	context = {}
	return render(request, 'Services/Promotion.html', context)

def AdviceList(request):
	context = {}
	return render(request, 'Services/AdviceList.html', context)

def PopUpViewAdvice(request):
	context = {}
	return render(request, 'Services/PopUpViewAdvice.html', context)

def SubService(request):
	context = {}
	return render(request, 'Services/SubService.html', context)
