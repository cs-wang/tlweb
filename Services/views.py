# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from db import models
import json
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import pytz

# Create your views here.

def DashBoard(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
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
	curpage = request.GET.get('p')
	if curpage==None:
		curpage="1"
	curpage = int(curpage)
	msgobj = models.Message()
	msglist,pagenum,totalnum = msgobj.myMessage("1", "1", sta, curpage)
	print "msglist:", msglist, pagenum, totalnum
	######################################################
	prevpage = (1 if curpage - 1 < 1 else curpage - 1)
	nextpage = (pagenum if curpage + 1 > pagenum else curpage + 1)
	interval = 5
	firstshowpage = (curpage-1)/interval*interval+1
	lastshowpage = (firstshowpage+interval if firstshowpage+interval < pagenum else pagenum+1)
	pageshowlist = range(firstshowpage, lastshowpage)
	
	if firstshowpage == 1:
		preomit = False
		prevomitpage = 1 #useless here
	else:
		preomit = True
		prevomitpage = (1 if firstshowpage-3 < 1 else firstshowpage-3)

	if lastshowpage >= pagenum+1:
		nextomit = False
		nextomitpage = pagenum #useless here
	else:
		nextomit = True
		nextomitpage = (pagenum if lastshowpage + 2 > pagenum else lastshowpage + 2)

	
	######################################################
	context = { 'msglist':msglist,
				'sta':sta,
				'pagenum':pagenum,
				'totalnum':totalnum,
				'pageshowlist':pageshowlist,
				'prevpage':prevpage,
				'curpage':curpage,
				'preomit':preomit,
				'nextomit':nextomit,
				'prevomitpage':prevomitpage,
				'nextomitpage':nextomitpage,
				'nextpage':nextpage }

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
# 	flag = member_.register('zdg',"赵镇辉啊","delegation_phone_","delegation_info_",\
# 		  "bind_phone_","pwd","weixinId","bank_","account_","cardHolder","receiver_","reciever_phone_",\
# 		  "receiver_addr_","order_Memo",1,0)   
	print member_.fixInfo(1,"改密码咯","新手机号码","新微信号码","新开户银行","新账户啊","新持卡人啊","新收货人啊","新收货电话啊","新收获地址啊")
	
	return render(request, 'Services/MemberEdit.html', context)

def MemberSave(request):
	RegUserId = request.POST['UserId']
	RegUserName = request.POST['UserName']
	RegNickName = request.POST['NickName']
	RegIDCard = request.POST['IDCard']
	RegUserStatus = request.POST['UserStatus']
	RegBindMob = request.POST['BindMob']
	RegDepositMobile = request.POST['DepositMobile']
	RegUserPwd = request.POST['UserPwd']
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
	print "RegUserId:",RegUserId
	print "RegUserName:",RegUserName
	print "RegNickName:",RegNickName
	print "RegIDCard:",RegIDCard
	print "RegUserStatus:",RegUserStatus
	print "RegBindMob:",RegBindMob
	print "RegDepositMobile:",RegDepositMobile
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
	memberobj = models.Member()
	if memberobj.register(RegUserName,RegNickName,RegDepositMobile,RegAlipay,RegBindMob,RegUserPwd,RegWeChat,RegBankName,RegBankAccount,
		RegTrueName,RegRecName,RegRecMob,RegRecAdd,RegMark,1,0) == True:
		obj = {'result':'t'}
	else:
		obj = {'result':'f',
			'msg':'用户名已经被注册'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

def MemberList(request):
	if request.session.get('role') == None or request.session['role'] != '1':
		return HttpResponseRedirect('/')
# 	naive = parse_datetime("2017-02-21 10:28:45")
#  	naive1 = parse_datetime("2016-04-01 10:28:45")
#  	time_ = pytz.timezone("UTC").localize(naive, is_dst=None)
#  	time_1 = pytz.timezone("UTC").localize(naive1, is_dst=None)
#  	memberlist,pageMax = member_.MemberList(1,user_or_phone_=None,member_status_=None,time_order_='0',reg_way='0',\
#                    reg_start_time_=None,reg_end_time_=None,conf_start_time_=None,conf_end_time_=time_1,pageNum=1)
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
	#context = {}
	curpage = request.GET.get('p')
	if curpage == None or curpage == '':
		curpage = "1"
	curpage = int(curpage)
	member_ = models.Member()
	memberlist,pagenum,totalnum = member_.MemberList(1,pageNum=curpage)
	######################################################
	prevpage = (1 if curpage - 1 < 1 else curpage - 1)
	nextpage = (pagenum if curpage + 1 > pagenum else curpage + 1)
	interval = 5
	firstshowpage = (curpage-1)/interval*interval+1
	lastshowpage = (firstshowpage+interval if firstshowpage+interval < pagenum else pagenum+1)
	pageshowlist = range(firstshowpage, lastshowpage)
	
	if firstshowpage == 1:
		preomit = False
		prevomitpage = 1 #useless here
	else:
		preomit = True
		prevomitpage = (1 if firstshowpage-3 < 1 else firstshowpage-3)

	if lastshowpage >= pagenum+1:
		nextomit = False
		nextomitpage = pagenum #useless here
	else:
		nextomit = True
		nextomitpage = (pagenum if lastshowpage + 2 > pagenum else lastshowpage + 2)

	
	######################################################
	context = { 'memberlist':memberlist,
				'pagenum':pagenum,
				'totalnum':totalnum,
				'pageshowlist':pageshowlist,
				'prevpage':prevpage,
				'curpage':curpage,
				'preomit':preomit,
				'nextomit':nextomit,
				'prevomitpage':prevomitpage,
				'nextomitpage':nextomitpage,
				'nextpage':nextpage }
	return render(request, 'Services/MemberList.html', context)

def SetAudit(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	context = {}
	return render(request, 'Services/SetAudit.html', context)

def MemberOrder(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')

	curpage = request.GET.get('p')
	if curpage == None or curpage == '':
		curpage = "1"
	curpage = int(curpage)

	orderobj=models.OrderForm()
	orderlist,pagenum,totalnum = orderobj.myServiceOrder(1, pageNum=curpage)
	print "orderlist",orderlist,pagenum
		######################################################
	prevpage = (1 if curpage - 1 < 1 else curpage - 1)
	nextpage = (pagenum if curpage + 1 > pagenum else curpage + 1)
	interval = 5
	firstshowpage = (curpage-1)/interval*interval+1
	lastshowpage = (firstshowpage+interval if firstshowpage+interval < pagenum else pagenum+1)
	pageshowlist = range(firstshowpage, lastshowpage)
	
	if firstshowpage == 1:
		preomit = False
		prevomitpage = 1 #useless here
	else:
		preomit = True
		prevomitpage = (1 if firstshowpage-3 < 1 else firstshowpage-3)

	if lastshowpage >= pagenum+1:
		nextomit = False
		nextomitpage = pagenum #useless here
	else:
		nextomit = True
		nextomitpage = (pagenum if lastshowpage + 2 > pagenum else lastshowpage + 2)
	
	######################################################
	context = { 'orderlist':orderlist,
				'pagenum':pagenum,
				'totalnum':totalnum,
				'pageshowlist':pageshowlist,
				'prevpage':prevpage,
				'curpage':curpage,
				'preomit':preomit,
				'nextomit':nextomit,
				'prevomitpage':prevomitpage,
				'nextomitpage':nextomitpage,
				'nextpage':nextpage }

#	naive = parse_datetime("2017-02-21 10:28:45")
# 	naive1 = parse_datetime("2016-04-01 10:28:45")
# 	time_ = pytz.timezone("UTC").localize(naive, is_dst=None)
# 	time_1 = pytz.timezone("UTC").localize(naive1, is_dst=None)	
#	order_ = models.OrderForm()
#	order_list,maxPage = order_.myServiceOrder(1,"123",'2',time_1,time_)
#	for i in order_list:
#		print i.order_id
#	print "最多", maxPage
#  	order_.createOrder(1,1,1000,1,"A+B都是货物啊","未发货")
#	order_.comfirmDelivery(1,"五环快递","1232131231232131231")
# 	print order_.myMemberOrder(1,time_1,time_,2)
	return render(request, 'Services/MemberOrder.html', context)

def Deliver(request):
	context = {}
	return render(request, 'Services/Deliver.html', context)


def UserMap(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	context = {}
	#member_ = models.Member()
	#memlist ,PageMax= member_.myMemberNet(1,'0',1)
	#for i in memlist:
	#	print i.user_id,i.user_name
	#print "最多",PageMax,"页"
	
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
# 	naive = parse_datetime("2017-02-21 10:28:45")
#   	naive1 = parse_datetime("2016-04-01 10:28:45")
#   	time_ = pytz.timezone("UTC").localize(naive, is_dst=None)
#   	time_1 = pytz.timezone("UTC").localize(naive1, is_dst=None)
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
# 	naive = parse_datetime("2016-03-21 10:28:45")
# 	time_ = pytz.timezone("UTC").localize(naive, is_dst=None)	
# 	adlist,maxPage =  advice_.my_advice(1,"0",None,None,time_,timezone.now())
# 	for i in adlist :
# 		print i.advice_id
# 	print "最多",maxPage
	advobj = models.Advice()
	advlist, pagenum = advobj.my_advice(2)
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
