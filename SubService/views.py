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

loginrole = '2'


def DashBoard(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	serviceid = request.session['service_id']
	numOfMember,numOfVip = models.members(service_id_=serviceid)
	context = { 'username':request.session['username'],
				'numOfMember':numOfMember,
				'numOfVip':numOfVip }
	return render(request, 'SubService/DashBoard.html', context)

def NoticeList(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	context = {'username':request.session['username'],}
	return render(request, 'SubService/NoticeList.html', context)

def MsgList(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	serviceid = request.session['service_id']
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
		id_ = serviceid, # service_id
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
				'username':request.session['username'],
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
	return render(request, 'SubService/MsgList.html', context)

def ViewMsg(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	msgid = request.GET.get('MsgId')
	msg_ = models.Message()
	msg = msg_.getFilterMsg(msgid)
	context = {	'msgtitle':msg.message_title,
				'msgcontent':msg.message_content,
				'msgid':msg.message_id, }
	return render(request, 'SubService/ViewMsg.html', context)

def MsgRead(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
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
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	context = {'username':request.session['username'],}
	return render(request, 'SubService/MemberEdit.html', context)
def MemberEdit1(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	reqUserId = request.GET.get('UserId')
	print "reqUserId:",reqUserId
	member_ = models.Member()
	selfinfo = member_.myInfo(int(reqUserId))
	print selfinfo.status.status_id
	context = { 'selfinfo':selfinfo,
				'UserId':reqUserId,
				'username':request.session['username'], }
	return render(request, 'SubService/MemberEdit1.html', context)

def MemberSave(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	serviceid = request.session['service_id']
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
	try :
		with transaction.atomic():
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
				serviceid = serviceid,
				referenceid = 0
				) == True:
				obj = {'result':'t'}
			else:
				obj = {'result':'f',
					'msg':'用户名已经被注册'}
	except BaseException,e:
		print e
		obj = {'result':'f',
					'msg':'用户名已经被注册'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

def MemberSave1(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
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
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	serviceid = request.session['service_id']
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
	memberlistnew,pagenum,totalnum = member_.MemberList(
		service_id_=serviceid,
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
	memberlist = []
	for onemember in memberlistnew:
		onerefer = member_.myInfo(onemember.reference_id)
		myreferlist1,pagenum1,totalnum1 = member_.myReference(user_id_ = onemember.user_id)
		onemember.refernum = totalnum1
		ones = (onemember, onerefer)
		memberlist.append(ones)
	print memberlist

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
				'username':request.session['username'],
				'reqUserInfo':reqUserInfo,
				'reqUserStatus':reqUserStatus,
				'reqorderby':reqorderby,
				'reqregfrom':reqregfrom,
				'reqregStart':reqregStart,
				'reqregEnd':reqregEnd,
				'reqsubStart':reqsubStart,
				'reqsubEnd':reqsubEnd,
				'reference_name':"",
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
	return render(request, 'SubService/MemberList.html', context)

def ViewMember(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	reqUserId = request.GET.get('UserId')
	print "reqUserId:",reqUserId
	context = {}
	return render(request, 'SubService/ViewMember.html', context)

def ViewMemberSelf(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	reqUserId = request.GET.get('UserId')
	print "reqUserId:",reqUserId
	member_ = models.Member()
	selfinfo = member_.myInfo(reqUserId)
	myreferlist,pagenum,totalnum = member_.myReference(user_id_ = reqUserId)
	refinfo = member_.myInfo(selfinfo.reference_id)
	print "selfinfo:",selfinfo
	context = {
		'selfinfo':selfinfo,
		'refinfo':refinfo,
		'totalnum':totalnum
	}
	return render(request, 'SubService/ViewMemberSelf.html', context)

def ViewReCome(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	reqUserId = request.GET.get('UserId')
	curpage = request.GET.get('p')
	if curpage == None or curpage == '':
		curpage = "1"
	curpage = int(curpage)
	if curpage <= 0:
		curpage = 1
	print "reqUserId:",reqUserId
	member_ = models.Member()
	myreferlist,pagenum,totalnum = member_.myReference(user_id_ = reqUserId, pageNum = curpage)
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
	context = {
				'UserId':reqUserId,
				'myreferlist':myreferlist,
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
	return render(request, 'SubService/ViewReCome.html', context)
# 激活
def SetAudit(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	context = {}
	return render(request, 'SubService/SetAudit.html', context)
# 审核
def SetAudit1(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	serviceid = request.session['service_id']
	reqUserId = request.POST.get('UserId')
	print "reqUserId:",reqUserId
	member_ = models.Member()
	try :
		with transaction.atomic():
			if member_.confirmMember(
		user_id_ = reqUserId, 
		service_id_ = serviceid
		)==True:
	
				obj = {'result':'t'}
			else:
				obj = {'result':'f',
					'msg':'请稍后再试！'}
	except BaseException,e:
		print e
		obj = {'result':'f',
					'msg':'请稍后再试！'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

def MemberOrder(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	serviceid = request.session['service_id']
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
	orderlist,pagenum,totalnum, totalmoney = orderobj.myMemberOrder(
			user_id_= reqUserId,
			service_id_=serviceid,
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
				'username':request.session['username'],
				'UserInfo':kreqUserInfo,
				'start':reqstart,
				'end':reqend,
				'OrderStatus':reqOrderStatus,
				'pagenum':pagenum,
				'totalnum':totalnum,
				'totalmoney':totalmoney,
				'pageshowlist':pageshowlist,
				'prevpage':prevpage,
				'curpage':curpage,
				'preomit':preomit,
				'nextomit':nextomit,
				'prevomitpage':prevomitpage,
				'nextomitpage':nextomitpage,
				'nextpage':nextpage }

	return render(request, 'SubService/MemberOrder.html', context)

def Deliver(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	reqids = request.GET.get('ids')
	orderidslist = reqids.split(',')
	orderformobj = models.OrderForm()
	orderinfolist = []
	for orderid in orderidslist:
		print "orderid:",orderid
		orderinfo = orderformobj.myDeliverInfoByOrderId(orderid)
		orderinfolist.append(orderinfo)
	context = { 'orderinfolist':orderinfolist}
	return render(request, 'SubService/Deliver.html', context)
import urllib
def DeliverSub(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	DeliverDatas = request.POST.get('data')
	#print "DeliverDatas:",DeliverDatas
	DeliverDataslist = DeliverDatas.split(',')
	orderformobj = models.OrderForm()
	obj = {}
	try :
		with transaction.atomic():
			for ddatas in DeliverDataslist:
				ddataslist = ddatas.split('|')
				expressname = ddataslist[1].replace('%','\\').decode('unicode-escape')
				orderformobj.comfirmDelivery(
					order_id_ = ddataslist[0],
					express_name_ = expressname,#unicode
					express_number_ = ddataslist[2]
				)
				
				obj = {'result':'t'}
	except BaseException,e:
		print e
		obj = {'result':'f',
			'msg':'请稍后再试！'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

def UserMap(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	context = {'username':request.session['username'],}
	return render(request, 'SubService/UserMap.html', context)

def GetMap(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	serviceid = request.session['service_id']
	reqUid = request.POST.get('Uid')
	reqstep = request.POST.get('step')

	print "reqUid:", reqUid
	print "reqstep:", reqstep
	memlist = []
	res = []
	memobj = models.Member()
	if reqUid == None:
		# memlist = memobj.myMemberNet(
		# 	userOrServiceid_=serviceid,
		# 	role_="0",
		# 	pageNum=1
		# 	)
		servicemem = models.Service.GetServiceName(servcie_id_ = serviceid)
		resmem =  {"UserId":0, "text":servicemem.service_name, "parentId":0,"type":"folder", "step":1, "Level":1, "Sort":0, "UserName":""}
		res.append(resmem)
	else:
		memlist = memobj.myMemberNet(
			userOrServiceid_=reqUid,
			role_="0", # here we find referenceid = userid  so keep role_ = "0"
			pageNum=1
			)
	for member in memlist:
		# print "================="
		# print member.user_id
		# print member.user_name
		# print member.reference_id
		# print member.service_id
		resmem =  {"UserId":member.user_id, "text":member.user_name, "parentId":member.reference_id,"type":"folder", "step":1, "Level":1, "Sort":0, "UserName":member.user_name}
		res.append(resmem)

	code = str(json.dumps(res))
	return HttpResponse(code)

def ComBank(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	serviceid = request.session['service_id']
	saobj = models.ServiceAccount()
	accountlist,pagenum,totalnum= saobj.comBank(
			service_id_=serviceid, 
			pageNum=1
			)
	print accountlist, pagenum, totalnum
	context = {
			'accountlist':accountlist,
			'username':request.session['username'],
			'pagenum':pagenum,
			'totalnum':totalnum
	}
	return render(request, 'SubService/ComBank.html', context)

def Promotion(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
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
	if reqSubStart == "" or reqSubStart == "None":
		reqSubStart = None
	if reqSubEnd == "" or reqSubEnd == "None":
		reqSubEnd = None
	if reqorderby == None:
		reqorderby = "0"
	if curpage == None or curpage == "":
		curpage = "1"
	curpage = int(curpage)
	if curpage <= 0:
		curpage = 1
	
	comsobj = models.CommissionOrder()
	comslist,pagenum,totalnum,totalmoney = comsobj.commissionList(
		user_name_=reqUserInfo,
		commission_status_=reqGiftStatus,
		commission_type_=reqGiftFrom,
		commission_created_start_=reqAddStart,
		commission_created_end_=reqAddEnd,
		commission_send_start_=reqSubStart,
		commission_send_end_=reqSubEnd,
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
				'username':request.session['username'],
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
				'totalmoney':totalmoney,
				'pageshowlist':pageshowlist,
				'prevpage':prevpage,
				'curpage':curpage,
				'preomit':preomit,
				'nextomit':nextomit,
				'prevomitpage':prevomitpage,
				'nextomitpage':nextomitpage,
				'nextpage':nextpage
				 }
	return render(request, 'SubService/Promotion.html', context)

def MoneyAudit(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
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
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
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
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	serviceid = request.session['service_id']
	print "service_id:", serviceid
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
							user_or_service_id_= serviceid,
							role_="1",
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
				'username':request.session['username'],
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

	return render(request, 'SubService/AdviceList.html', context)

def AdviceView(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	advid = request.GET.get('id')
	print "advid:",advid
	advobj = models.Advice()
	adv = advobj.one_advice(advid)
	context = { 'adv':adv,
			    'username':request.session['username'],
			   }
	return render(request, 'SubService/AdviceView.html', context)

def AdviceSub(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	serviceid = request.session['service_id']
	advid = request.POST.get('id')
	advcon = request.POST.get('info')
	print "advcon:",advcon
	advobj = models.Advice()
	advobj.reply_advice(	
			user_id_ = 1, #useless
			reply_content_ = advcon,
			service_id_ = serviceid, # useless
			advice_id_ = advid   
			)
	advice = advobj.one_advice(advid)
	if advice.advice_status == "1":
		obj = {'result':'t'}
	else:
		obj = {'result':'f'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

def SubService(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	serviceid = request.session['service_id']
	print "ServiceID:",serviceid
	serobj = models.Service()
	subserviceobj =  serobj.getSecService(service_id_ = serviceid)
	print "subserviceobj:",subserviceobj.service_id
	context = {}
	if subserviceobj != None:
		context = { "subserviceobj":subserviceobj,
					'username':request.session['username'], }
	return render(request, 'SubService/SubService.html', context)

def SubServiceSave(request):
	if request.session.get('role') == None or request.session['role'] != loginrole:
		return HttpResponseRedirect('/')
	UserId = request.POST.get('UserId')
	ServiceName = request.POST.get('ServiceName')
	ServiceAdminName = request.POST.get('ServiceAdminName')
	UserName = request.POST.get('UserName')
	UserPwd = request.POST.get('UserPwd')
	UserStatus = request.POST.get('UserStatus')
	ServiceMark = request.POST.get('ServiceMark')

	print "UserId:",UserId
	print "ServiceName:",ServiceName
	print "ServiceAdminName:",ServiceAdminName
	print "UserName:",UserName
	print "UserPwd:",UserPwd
	print "UserStatus:",UserStatus
	print "ServiceMark:",ServiceMark

	serobj = models.Service()
	ret = serobj.saveSecService(
			service_name_ = UserName,
			service_pwd_ = UserPwd,
			service_role_ = UserStatus,
			service_area_ = ServiceName,
            service_ref_ = UserId,
            service_response_ = ServiceAdminName,
            service_memo_ = ServiceMark
            )

	if ret == True:
		obj = {'result':'t'}
	else:
		obj = {'result':'f',
			'msg':"用户名已经被注册"}
	code = str(json.dumps(obj))
	return HttpResponse(code)