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

# Create your views here.
import urllib2


def DashBoard(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
# 	send_Short_Message(15757116149,"zzh")
# 	time = timezone.now()
#     	time_1 = timezone.now()-datetime.timedelta(days=30)
# 	print time
# 	print time_1
   	oc = models.CommissionOrder()
   	oc.leadercommission(1)
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
	msglist,pagenum,totalnum = msgobj.myMessage( 
		id_ = 1, # service_id
		role_="1", # 服务中心
		message_status_ = sta, 
		pageNum = curpage
		)
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
	return render(request, 'Services/MemberEdit.html', context)

def MemberEdit1(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	reqUserId = request.GET.get('UserId')
	print "reqUserId:",reqUserId
	member_ = models.Member()
	selfinfo = member_.myInfo(int(reqUserId))
	print selfinfo.status.status_id
	context = { 'selfinfo':selfinfo,
				'UserId':reqUserId }
	return render(request, 'Services/MemberEdit1.html', context)

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
	if memberobj.register(
				user = RegUserName,
				nickname_ = RegNickName,
				delegation_phone_ = RegDepositMobile,
				delegation_info_ = RegAlipay,
				bind_phone_ = RegBindMob,
				pwd = RegUserPwd,
				weixinId = RegWeChat,
				bank_ = RegBankName,
				account_ = RegBankAccount,
				cardHolder = RegTrueName,
				receiver_ = RegRecName,
				reciever_phone_ = RegRecMob,
				receiver_addr_ = RegRecAdd,
				order_Memo_ = RegMark,
				serviceid = 1,
				referenceid = 0
				) == True:
		obj = {'result':'t'}
	else:
		obj = {'result':'f',
			'msg':'用户名已经被注册'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

def MemberSave1(request):
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
	#RegMark = request.POST['Mark']
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
	#print "RegMark:",RegMark
	if RegUserPwd == "":
		RegUserPwd = None

	memberobj = models.Member()
	if memberobj.fixInfo(
				user_id_ = RegUserId,
				pwd_ = RegUserPwd,
				bind_phone_ = RegBindMob,
				weixinId_ = RegWeChat,
				bank_ = RegBankName,
				account_ = RegBankAccount,
				card_holder_ = RegTrueName,
				receiver_ = RegRecName,
				receiver_phone_ = RegRecMob,
				receiver_addr_ = RegRecAdd,
				member_status_ = RegUserStatus
				) == True:
		obj = {'result':'t'}
	else:
		obj = {'result':'f',
			'msg':'请稍后再试！'}
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
	sesserviceid = request.session.get('service_id')
	reqUserInfo = request.GET.get('UserInfo')
	reqUserStatus = request.GET.get('UserStatus')
	reqorderby = request.GET.get('orderby')
	reqregfrom = request.GET.get('regfrom')
	reqregStart = request.GET.get('regStart')
	reqregEnd = request.GET.get('regEnd')
	reqsubStart = request.GET.get('subStart')
	reqsubEnd = request.GET.get('subEnd')

	kreqUserInfo = reqUserInfo
	kreqUserStatus = reqUserStatus
	kreqorderby = reqorderby
	kreqregfrom = reqregfrom
	kreqregStart = reqregStart
	kreqregEnd = reqregEnd
	kreqsubStart = reqsubStart
	kreqsubEnd = reqsubEnd

	curpage = request.GET.get('p')
	if reqUserInfo=="" or reqUserInfo=="None":
		reqUserInfo=None
	if reqUserStatus=="0" or reqUserStatus=="None":
		reqUserStatus=None
	if reqorderby==None or reqorderby=="None":
		reqorderby="0"
	if reqregfrom==None or reqregfrom=="None":
		reqregfrom="0"
	if reqregStart=="" or reqregStart== "None":
		reqregStart=None
	if reqregEnd=="" or reqregEnd=="None":
		reqregEnd=None
	if reqsubStart=="" or reqsubStart=="None":
		reqsubStart=None
	if reqsubEnd=="" or reqsubEnd == "None":
		reqsubEnd=None
	if curpage == None or curpage == '':
		curpage = "1"
	if reqUserStatus!=None:
		kreqUserStatus = int(reqUserStatus)
	else:
		kreqUserStatus = reqUserStatus
	curpage = int(curpage)
	print "sesserviceid:",sesserviceid
	print "reqUserInfo:",reqUserInfo
	print "reqUserStatus:",kreqUserStatus
	print "reqorderby:",reqorderby
	print "reqregfrom:",reqregfrom
	print "reqregStart:",reqregStart
	print "reqregEnd:",reqregEnd
	print "reqsubStart:",reqsubStart
	print "reqsubEnd:",reqsubEnd
	
	member_ = models.Member()
	memberlist,pagenum,totalnum = member_.MemberList(
		service_id_=1,
		user_or_phone_=reqUserInfo,
		member_status_=kreqUserStatus,
		time_order_=reqorderby,
		reg_way=reqregfrom,
		reg_start_time_=reqregStart,
		reg_end_time_=reqregEnd,
		conf_start_time_=reqsubStart,
		conf_end_time_=reqsubEnd,
		pageNum=curpage
		)
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
				'reqUserInfo':reqUserInfo,
				'reqUserStatus':reqUserStatus,
				'reqorderby':reqorderby,
				'reqregfrom':reqregfrom,
				'reqregStart':reqregStart,
				'reqregEnd':reqregEnd,
				'reqsubStart':reqsubStart,
				'reqsubEnd':reqsubEnd,
				'reference_name':"张大爷",
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

def ViewMember(request):
	reqUserId = request.GET.get('UserId')
	print "reqUserId:",reqUserId
	context = {}
	return render(request, 'Services/ViewMember.html', context)

def ViewMemberSelf(request):
	reqUserId = request.GET.get('UserId')
	print "reqUserId:",reqUserId
	member_ = models.Member()
	selfinfo = member_.myInfo(reqUserId)
	print "selfinfo:",selfinfo
	context = {
		'selfinfo':selfinfo,
	}
	return render(request, 'Services/ViewMemberSelf.html', context)

def ViewReCome(request):
	reqUserId = request.GET.get('UserId')
	print "reqUserId:",reqUserId
	member_ = models.Member()
	selfinfo = member_.myInfo(reqUserId)
	print "selfinfo:",selfinfo
	context = {
		'selfinfo':selfinfo,
	}
	return render(request, 'Services/ViewReCome.html', context)
# 激活
def SetAudit(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	context = {}
	return render(request, 'Services/SetAudit.html', context)
# 审核
def SetAudit1(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	reqUserId = request.POST.get('UserId')
	print "reqUserId:",reqUserId
	member_ = models.Member()
	if member_.confirmMember(
		user_id_ = reqUserId, 
		service_id_ = 1
		)==True:
	
		obj = {'result':'t'}
	else:
		obj = {'result':'f',
			'msg':'请稍后再试！'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

def MemberOrder(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	reqUserId = request.GET.get('UserId')
	reqUserInfo = request.GET.get('UserInfo')
	reqOrderStatus = request.GET.get('OrderStatus')
	reqstart = request.GET.get('start')
	reqend = request.GET.get('end')
	curpage = request.GET.get('p')

	kreqUserInfo = reqUserInfo
	kreqOrderStatus = reqOrderStatus
	kreqstart = reqstart
	kreqend = reqend

	if reqUserInfo=="" or reqUserInfo == "None":
		reqUserInfo=None
	if reqOrderStatus==None:
		reqOrderStatus = "2"
	if reqstart=="" or reqstart == "None":
		reqstart=None
	if reqend=="" or reqend == "None":
		reqend=None
	if curpage == None or curpage == "":
		curpage = "1"
	curpage = int(curpage)

	print "reqUserId:",reqUserId
	print "reqUserInfo:",reqUserInfo
	print "reqOrderStatus:",reqOrderStatus

	orderobj=models.OrderForm()
	orderlist,pagenum,totalnum = orderobj.myMemberOrder(
			user_id_= reqUserId,
			service_id_=1,
			user_or_phone_=reqUserInfo,
			order_type_=reqOrderStatus,
			start_time_=reqstart,
			end_time_=reqend,
			pageNum=curpage)

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
				'UserInfo':kreqUserInfo,
				'start':reqstart,
				'end':reqend,
				'OrderStatus':reqOrderStatus,
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
	reqids = request.GET.get('ids')
	orderidslist = reqids.split(',')
	orderformobj = models.OrderForm()
	orderinfolist = []
	for orderid in orderidslist:
		print "orderid:",orderid
		orderinfo = orderformobj.myDeliverInfoByOrderId(orderid)
		orderinfolist.append(orderinfo)
	context = { 'orderinfolist':orderinfolist}
	return render(request, 'Services/Deliver.html', context)
import urllib
def DeliverSub(request):
	DeliverDatas = request.POST.get('data')
	#print "DeliverDatas:",DeliverDatas
	DeliverDataslist = DeliverDatas.split(',')
	orderformobj = models.OrderForm()
	for ddatas in DeliverDataslist:
		ddataslist = ddatas.split('|')
		expressname = ddataslist[1].replace('%','\\').decode('unicode-escape')
		orderformobj.comfirmDelivery(
					order_id_ = ddataslist[0],
					express_name_ = expressname,#unicode
					express_number_ = ddataslist[2]
				)
	if True:
		obj = {'result':'t'}
	else:
		obj = {'result':'f',
			'msg':'请稍后再试！'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

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
