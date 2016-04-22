# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db import transaction
from db import models
import datetime
import json
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import pytz

# Create your views here.
import urllib2
@transaction.atomic
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
	if curpage <= 0:
		curpage = 1

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
@transaction.atomic
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
	if curpage <= 0:
		curpage = 1

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
@transaction.atomic
def SetAudit1(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
# 	reqUserId = request.POST.get('UserId')
# 	print "reqUserId:",reqUserId
	member_ = models.Member()
# 	if member_.confirmMember(
# 		user_id_ = reqUserId, 
# 		service_id_ = 1
# 		)==True:
# 	
# 		obj = {'result':'t'}
# 	else:
# 		obj = {'result':'f',
# 			'msg':'请稍后再试！'}
# 	code = str(json.dumps(obj))
# 	return HttpResponse(code)
	
	return render(request, 'Services/SetAudit.html', context)
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
	if curpage <= 0:
		curpage = 1

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
	return render(request, 'Services/UserMap.html', context)

def GetMap(request):
	reqUid = request.POST.get('Uid')
	reqstep = request.POST.get('step')

	print "reqUid:", reqUid
	print "reqstep:", reqstep
	memlist = []
	res = []
	memobj = models.Member()
	serviceid = 1;
	if reqUid == None:
		memlist = memobj.myMemberNet(
			userOrServiceid_=serviceid,
			role_="0",
			pageNum=1
			)
	else:
		memlist = memobj.myMemberNet(
			userOrServiceid_=reqUid,
			role_="1",
			pageNum=1
			)
	for member in memlist:
		# print "================="
		# print member.user_id
		# print member.user_name
		# print member.reference_id
		# print member.service_id
		resmem =  {"UserId":member.user_id, "text":member.nickname, "parentId":member.reference_id,"type":"folder", "step":1, "Level":1, "Sort":0, "UserName":member.user_name}
		res.append(resmem)

	code = str(json.dumps(res))
	return HttpResponse(code)

def ComBank(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	serviceid = 1;
	saobj = models.ServiceAccount()
	accountlist,pagenum,totalnum= saobj.comBank(
			service_id_=1, 
			pageNum=1
			)
	print accountlist, pagenum, totalnum
	context = {
			'accountlist':accountlist,
			'pagenum':pagenum,
			'totalnum':totalnum
	}
	return render(request, 'Services/ComBank.html', context)

def Promotion(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	# UserInfo=&GiftStatus=4&GiftFrom=-1&AddStart=&AddEnd=&SubStart=&SubEnd=&orderby=1
	reqUserInfo = request.GET.get('UserInfo')
	reqGiftStatus = request.GET.get('GiftStatus')
	reqGiftFrom = request.GET.get('GiftFrom')
	reqAddStart = request.GET.get('AddStart')
	reqAddEnd = request.GET.get('AddEnd')
	reqSubStart = request.GET.get('SubStart')
	reqSubEnd = request.GET.get('SubEnd')
	reqorderby = request.GET.get('orderby')
	curpage = request.GET.get('p')

	print "reqUserInfo:",reqUserInfo
	print "reqGiftStatus:",reqGiftStatus
	print "reqGiftFrom:",reqGiftFrom
	print "reqAddStart:",reqAddStart
	print "reqAddEnd:",reqAddEnd
	print "reqorderby:",reqorderby
	if reqUserInfo == "" or reqUserInfo == "None":
		reqUserInfo = None
	if reqGiftStatus == "3" or reqGiftStatus == "None":
		reqGiftStatus =  None
	if reqGiftFrom == "6" or reqGiftFrom == "None":
		reqGiftFrom = None
	if reqAddStart == "" or reqAddStart == "None":
		reqAddStart = None
	if reqAddEnd == "" or reqAddEnd == "None":
		reqAddEnd = None
	if reqorderby == None:
		reqorderby = "0"
	if curpage == None or curpage == "":
		curpage = "1"
	curpage = int(curpage)
	if curpage <= 0:
		curpage = 1
	
	comsobj = models.CommissionOrder()
	comslist,pagenum,totalnum = comsobj.commissionList(
		user_name_=reqUserInfo,
		commission_status_=reqGiftStatus,
		commission_type_=reqGiftFrom,
		commision_created_start_=reqAddStart,
		commision_created_end_=reqAddEnd,
		time_order_=reqorderby,
		pageNum=curpage)
	#for coms in comslist:
		#print "comstye:",coms.commission_type
		#print "time:",coms.commission_created

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
	context = {	'comslist':comslist,
				'UserInfo':reqUserInfo,
				'GiftStatus':reqGiftStatus,
				'GiftFrom':reqGiftFrom,
				'AddStart':reqAddStart,
				'AddEnd':reqAddEnd,
				'SubStart':reqSubStart,
				'SubEnd':reqSubEnd,
				'orderby':reqorderby,
				'pagenum':pagenum,
				'totalnum':totalnum,
				'pageshowlist':pageshowlist,
				'prevpage':prevpage,
				'curpage':curpage,
				'preomit':preomit,
				'nextomit':nextomit,
				'prevomitpage':prevomitpage,
				'nextomitpage':nextomitpage,
				'nextpage':nextpage
				 }
	return render(request, 'Services/Promotion.html', context)

def MoneyAudit(request):
	reqids = request.POST.get('ids')
	comsidlist = reqids.split(',')
	comsobj = models.CommissionOrder()
	for comsid in comsidlist:
		print comsid
		comsobj.confirmComm(commission_id_ = comsid)
	obj = {'result':'t'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

def MoneySub(request):
	reqids = request.POST.get('ids')
	comsidlist = reqids.split(',')
	comsobj = models.CommissionOrder()
	for comsid in comsidlist:
		print comsid
		comsobj.deliverComm(commission_id_ = comsid)
	obj = {'result':'t'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

def AdviceList(request):
	if request.session['role'] != '1':
		return HttpResponseRedirect('/')
	
	reqtitle = request.GET.get('title')
	reqserviceReadStatus = request.GET.get('serviceReadStatus')
	reqadminReadStatus = request.GET.get('adminReadStatus')
	reqaddStart = request.GET.get('addStart')
	reqAddEnd = request.GET.get('AddEnd')
	curpage = request.GET.get('p')

	print "reqtitle:",reqtitle
	print "reqserviceReadStatus:",reqserviceReadStatus
	print "reqadminReadStatus:",reqadminReadStatus
	print "reqaddStart:",reqaddStart
	print "reqAddEnd:",reqAddEnd
	print "curpage:",curpage

	if reqtitle == "" or reqtitle == "None":
		reqtitle = None
	if reqserviceReadStatus == "2" or reqserviceReadStatus == "None":
		reqserviceReadStatus = None
	if reqadminReadStatus == "2" or reqadminReadStatus == "None":
		reqadminReadStatus = None
	if reqaddStart == "" or reqaddStart == "None":
		reqaddStart = None
	if reqAddEnd == "" or reqAddEnd == "None":
		reqAddEnd = None
	if curpage == None or curpage == "":
		curpage = "1"
	curpage = int(curpage)
	if curpage <= 0:
		curpage = 1

	advobj = models.Advice()
	advlist,pagenum,totalnum = advobj.my_advice(
							user_or_service_id_= 1,
							role_="0",
							title_ = reqtitle,
							advice_status_ = reqserviceReadStatus,
                  			time_start_ = reqaddStart,
                  			time_end_ = reqAddEnd,
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
	print "my_advice:",advlist
	context = {	'advlist':advlist,
				'title':reqtitle,
				'serviceReadStatus':reqserviceReadStatus,
				'adminReadStatus':reqadminReadStatus,
				'addStart':reqaddStart,
				'AddEnd':reqAddEnd,
				'pagenum':pagenum,
				'totalnum':totalnum,
				'pageshowlist':pageshowlist,
				'prevpage':prevpage,
				'curpage':curpage,
				'preomit':preomit,
				'nextomit':nextomit,
				'prevomitpage':prevomitpage,
				'nextomitpage':nextomitpage,
				'nextpage':nextpage
						}

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
