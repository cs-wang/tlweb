# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import pytz
# Create your views here.
import json
from db import models
from urllib2 import Request
from django.template.defaultfilters import title
def DashBoard(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	user_id=request.session['user_id']
	print user_id
	memberobj = models.Member()
	myinfo=memberobj.myInfo(user_id)
	print myinfo.user_name
	print myinfo.nickname
	#print myinfo.status_id
	memstatus=models.MemberStatus();
	status_desc=memstatus.getStatusDesc(myinfo.status_id).status_desc
	print status_desc
	print str(myinfo.register_time)[0:19]
	print str(myinfo.confirm_time)[0:19]
	context = {'user_name':myinfo.user_name,'nickname':myinfo.nickname,'status_desc':status_desc,'count':5,\
			           'regist_time':str(myinfo.register_time)[0:19],'confirm_time':str(myinfo.confirm_time)[0:19]}
	return render(request, 'Member/DashBoard.html', context)

def ReConsume(request):
	context = {}
	return render(request, 'Member/ReConsume.html', context)

def ReConsumeSave(request):
	context = {}
	obj = {'result':'t'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

def MsgList(request):
	print "msg list"
	if request.session['role'] == None:
		return HttpResponseRedirect('/')
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	user_id=request.session['user_id']
	print 'user_id='+str(user_id)
	username=request.session['username']
	msgobj=models.Message()
	if request.GET.get("status","") != "":
		status=request.GET["status"]
	else:
		status='2'
	curpage = request.GET.get('p')
	if curpage == None:
			curpage='1';
	curpage=int(curpage)
	if curpage<=0:
		curpage=0
	msglist,pagenum,totalnum = msgobj.myMessage( 
		user_id,
		role_="0", # 服务中心
		message_status_ = status, 
		pageNum = curpage
		)
	print status
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
		
	context = { 'msg_list':msglist,
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
	
	print user_id
	print len(msglist)
	for msg in msglist:
	    print msg.message_title+str(msg.sent_time)[0:19]
	#context = {'msg_list':msglist,'username':username}
	context['username']=username
	context['status']=status
	context['count']=totalnum
	return render(request, 'Member/MsgList.html', context)


def ViewMsg(request):
	message_id=int(request.GET["MsgId"])
	print 'message_id='+str(message_id)
	msgobj=models.Message()
	msg=msgobj.getFilterMsg(message_id)
	print msg.message_title+"  "+msg.message_content
	context={'message_id':message_id,'message_title':msg.message_title,'message_content':msg.message_content}
	return render(request,'Member/ViewMsg.html',context)
def MsgRead(request):
	print 'Message_read'
	message_id=request.POST.get('MsgId')
	msgobj=models.Message()
	msgobj.readMessage(message_id)
	msg=msgobj.getFilterMsg(message_id)
	if msg.message_status == '1':
		obj = {'result':'t'}
	else:
		obj = {'result':'f'}
	code = str(json.dumps(obj))
	return HttpResponse(code)

def ShowModel(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	username=request.session['username']
	
	context = {'username':username}
	return render(request, 'Member/ShowModel.html', context)
 
def ComBank(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	username=request.session['username']
	user_id=request.session['user_id']
	memobj=models.Member()
	service_id=memobj.myInfo(user_id).service_id
	print 'user_id='+str(user_id)
	print 'service_id='+str(service_id)
	serviceobj=models.Service()
	service_info=serviceobj.getServiceInfo(service_id)
	ser_acc_obj=models.ServiceAccount()
	service_account_list=ser_acc_obj.comBankAll(service_id)
	infolist=[]
	for service_account in service_account_list:
		account={'bank':service_account.bank+'('+service_info.service_area+')','bank_account':service_account.bank_account,'holder':service_account.card_holder,\
			'phone':service_account.phone+'('+service_info.service_area+')'}
		infolist.append(account)
	context={'username':username,'infolist':infolist,'totalnum':len(infolist)}
	return render(request, 'Member/ComBank.html', context)

def MemberOrder(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	order_status=request.GET.get('OrderStatus')
	if order_status == None:
		order_status='2'
	username=request.session['username']
	user_id=request.session['user_id']
	start_time=request.GET.get('start')
	if start_time != None:
		if start_time == 'None': 
			start_time=None
	
	
	end_time=request.GET.get('end')
	if end_time!=None:
		if end_time == 'None':
			end_time=None
	
	member_ = models.OrderForm()

	money=0;
	
	curpage = request.GET.get('p')
	if curpage == None:
			curpage='1';
	curpage=int(curpage)
	if curpage<=0:
		curpage=1
	print 'cur='+str(curpage)
	ordlist,pagenum,totalnum = member_.myMemberOrder( 
		user_id,
		None,
		None,
		order_status, 
		start_time,
		end_time,
		curpage
		)
	
	for order in ordlist:
		money+=order.order_price
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
		
	context = {
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
	context['username']=username
	context['ordlist']=ordlist
	context['order_status']=order_status
	context['start_time']=start_time
	context['end_time']=end_time
	context['money']=money
	
	return render(request, 'Member/MemberOrder.html', context)

def RewardOrder(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	username=request.session['username']
	user_id=request.session['user_id']
	comissionobj=models.CommissionOrder()
	money=0
	type=request.GET.get('type')
	print 'type:',type
	if type == None:
		type='1'
	print 'type:',type
	
	curpage = request.GET.get('p')
	if curpage == None:
			curpage='1';
	curpage=int(curpage)
	if curpage<=0:
		curpage=1
	print 'cur='+str(curpage)
	comissionlist,pagenum,totalnum=comissionobj.commissionList(username,type,None,None,None,'0',curpage)
	
	
	for comission in comissionlist:
		money+=comission.commission_price
	print 'money:',money
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
		
	context = {
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
	context['username']=username
	context['comissionlist']=comissionlist
	context['type']=type
	context['money']=money
	
	return render(request, 'Member/RewardOrder.html', context)

def RewardOrderList(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	username=request.session['username']
	user_id=request.session['user_id']
	comissionobj=models.CommissionOrder()
	money=0
	type=request.GET.get('type')
	print 'type:',type
	if type == None:
		type='1'
	print 'type:',type
	
	curpage = request.GET.get('p')
	if curpage == None:
			curpage='1';
	curpage=int(curpage)
	if curpage<=0:
		curpage=1
	print 'cur='+str(curpage)
	comissionlist,pagenum,totalnum=comissionobj.commissionList(username,type,None,None,None,'0',curpage)
	
	
	for comission in comissionlist:
		money+=comission.commission_price
	print 'money:',money
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
		
	context = {
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
	context['username']=username
	context['comissionlist']=comissionlist
	context['type']=type
	context['money']=money
	return render(request, 'Member/RewardOrderList.html', context)

def Recome(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	username=request.session['username']
	user_id=request.session['user_id']
	memobj=models.Member()
	service_id=memobj.myInfo(user_id).service_id
	print 'user_id='+str(user_id)
	print 'service_id='+str(service_id)
	serviceobj=models.Service()
	service_info=serviceobj.getServiceInfo(service_id)
	ser_acc_obj=models.ServiceAccount()
	service_account_list=ser_acc_obj.comBankAll(service_id)
	infolist=[]
	for service_account in service_account_list:
		account={'bank':service_account.bank+'('+service_info.service_area+')','bank_account':service_account.bank_account,'holder':service_account.card_holder,\
			'phone':service_account.phone+'('+service_info.service_area+')'}
		infolist.append(account)
	context={'username':username,'infolist':infolist}
	return render(request, 'Member/Recome.html', context)

def RecomeSave(request):
	#RegUserId = request.POST['UserId']
	RegUserName = request.POST['UserName']
	RegNickName = request.POST['NickName']
	RegDepositMobile=request.POST['DepositMobile']
	RegAlipay = request.POST['Alipay']
	RegBindMob=request.POST['BindMob']
	RegUserPwd=request.POST['UserPwd']
	RegWeChat=request.POST['WeChat']
	RegBankName = request.POST['BankName']
	RegBankAccount = request.POST['BankAccount']
	RegTrueName = request.POST['TrueName']
	RegRecName = request.POST['RecName']
	RegRecMob = request.POST['RecMob']
	RegRecAdd = request.POST['RecAdd']
	RegMark=request.POST['Mark']
	RegRefId=request.session['user_id']
	
	#RegMark = request.POST['Mark']
	#print "RegUserId:",RegUserId
	print "RegUserName:",RegUserName
	print "RegNickName:",RegNickName
	print "RegDepositMobile:",RegDepositMobile
	print "RegAlipay:",RegAlipay
	print "RegBindMob:",RegBindMob
	print "RegUserPwd:",RegUserPwd
	print "RegWeChat:",RegWeChat
	print "RegBankName:",RegBankName
	print "RegBankAccount:",RegBankAccount
	print "RegTrueName:",RegTrueName
	print "RegRecName:",RegRecName
	print "RegRecMob:",RegRecMob
	print "RegRecAdd:",RegRecAdd
	print 'RegMark:',RegMark
	print 'RegRefId:',RegRefId
	memobj=models.Member()
	service_id=memobj.myInfo(RegRefId).service_id
	flag=memobj.register(RegUserName,RegNickName,RegDepositMobile,RegAlipay,RegBindMob,RegUserPwd,RegWeChat,RegBankName,\
						RegBankAccount,RegTrueName,RegRecName,RegRecMob,RegRecAdd,RegMark,service_id,RegRefId)
	#register(self,user,nickname_,delegation_phone_,delegation_info_,\
     #    bind_phone_,pwd,weixinId,bank_,account_,cardHolder,receiver_,reciever_phone_,\
       #  receiver_addr_,order_Memo_,serviceid,referenceid):
	
	#print "RegMark:",RegMark
	if RegUserPwd == "":
		RegUserPwd = None

	if flag:
		print '推荐成功'
		obj={'result':'t'}
	else:
		obj = {'result':'f','msg':'请稍后再试！'}
	code = str(json.dumps(obj))
	print code
	return HttpResponse(code)

def RecomeList(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	username=request.session['username']
	user_id=request.session['user_id']
	memobj=models.Member()
	curpage = request.GET.get('p')
	if curpage == None:
			curpage='1';
	curpage=int(curpage)
	if curpage<=0:
		curpage=1
	print 'cur='+str(curpage)
	reflist,pagenum,totalnum = memobj.myReference( 
		user_id,
		curpage
		)
	refInfolist=[]
	for ref in reflist:
		print ref.user_id
		refcount=memobj.myReference(ref.user_id)[2]
		refInfo={'nickname':ref.nickname,'bind_phone':ref.bind_phone,'regist_time':ref.register_time,'confirm_time':ref.confirm_time,'ref_num':refcount}
		refInfolist.append(refInfo)
	print pagenum,totalnum
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
		
	context = {
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
	#context = {'username':username}
	context['username']=username
	context['refInfolist']=refInfolist
	
	return render(request, 'Member/RecomeList.html', context)

def MyRecomeAll(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	user_id=request.session['user_id']
	username=request.session['username']
	memobj=models.Member()
	type=request.GET.get('type')
	print 'type:',type
	if type == None:
		type='1'
	print 'type:',type
	curpage = request.GET.get('p')
	if curpage == None:
			curpage='1';
	curpage=int(curpage)
	if curpage<=0:
		curpage=1
	print 'cur='+str(curpage)
	if  type == '0':
		reclist,pagenum,totalnum = memobj.myIndirectRef( 
		user_id,
		curpage
		)
	else :
		reclist,pagenum,totalnum = memobj.myReference( 
		user_id,
		curpage
		)
	
	print pagenum,totalnum
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
		
	context = {
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
	context['username']=username
	context['type']=type
	context['reclist']=reclist
#	member_ = models.Member()
#	list ,maxPage = member_.myReference(1,1)
	#print list
	#print "最多",maxPage
	return render(request, 'Member/MyRecomeAll.html', context)
def UserMap(request):
	username=request.session['username']
	context={}
	context['username']=username
	context["level"]=0
	return render(request, 'Member/UserMap.html', context)


def GetMap(request):
	reqUid = request.POST.get('Uid')
	reqstep = request.POST.get('step')

	print "get in get map"
	print "reqUid:", reqUid
	print "reqstep:", reqstep
	memlist = []
	res = []
	memobj = models.Member()
	serviceid = 1;
	if reqUid == None:
		serviceid=request.session['user_id']
		reqstep=0
		memlist = memobj.myMemberNet(
			userOrServiceid_=serviceid,
			role_="0",
			pageNum=1
			)
	else:
		if int(reqstep)<3 :
			memlist = memobj.myMemberNet(
										userOrServiceid_=reqUid,
										role_="1",
										pageNum=1
										)
		else:
			memlist={}
	for member in memlist:
		resmem =  {"UserId":member.user_id, "text":member.nickname, "parentId":member.reference_id,"type":"folder", "step":int(reqstep)+1, "Level":1, "Sort":0, "UserName":member.user_name}
		res.append(resmem)

	code = str(json.dumps(res))
	#print code
	return HttpResponse(code)


def MyData(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	username=request.session['username']
	user_id=request.session['user_id']
	memobj=models.Member()
	meminfo=memobj.myInfo(user_id)
	if meminfo.status_id == 2:
		modifiable='0'
	else:
		modifiable='1'
	print modifiable
	
	context = {}
	context['username']=username
	context['modifiable']=modifiable
	context['meminfo']=meminfo
	return render(request, 'Member/MyData.html', context)
def MyDataUpdate(request):
	user_id=request.session["user_id"]
	RegUserName = request.POST['UserName']
	RegNickName = request.POST['NickName']
	RegDepositMobile=request.POST['DepositMobile']
	RegAlipay = request.POST['Alipay']
	RegBindMob=request.POST['BindMob']
	RegUserPwd=request.POST['UserPwd']
	RegWeChat=request.POST['WeChat']
	RegBankName = request.POST['BankName']
	RegBankAccount = request.POST['BankAccount']
	RegTrueName = request.POST['TrueName']
	RegRecName = request.POST['RecName']
	RegRecMob = request.POST['RecMob']
	RegRecAdd = request.POST['RecAdd']
	
	#RegMark = request.POST['Mark']
	#print "RegUserId:",RegUserId
	print "RegUserName:",RegUserName
	print "RegNickName:",RegNickName
	print "RegDepositMobile:",RegDepositMobile
	print "RegAlipay:",RegAlipay
	print "RegBindMob:",RegBindMob
	print "RegUserPwd:",RegUserPwd
	print "RegWeChat:",RegWeChat
	print "RegBankName:",RegBankName
	print "RegBankAccount:",RegBankAccount
	print "RegTrueName:",RegTrueName
	print "RegRecName:",RegRecName
	print "RegRecMob:",RegRecMob
	print "RegRecAdd:",RegRecAdd
	memobj=models.Member()
	#fixInfo(self,user_id_,pwd_=None,bind_phone_=None,weixinId_=None,bank_=None,account_=None,card_holder_=None,\
      #          receiver_=None,receiver_phone_=None,receiver_addr_=None,member_status_ =None):
	flag=memobj.fixInfo(user_id,RegUserPwd,RegBindMob,RegWeChat,RegBankName,RegBankAccount,RegTrueName,RegRecName,RegRecMob,RegRecAdd)
	#register(self,user,nickname_,delegation_phone_,delegation_info_,\
     #    bind_phone_,pwd,weixinId,bank_,account_,cardHolder,receiver_,reciever_phone_,\
       #  receiver_addr_,order_Memo_,serviceid,referenceid):
	
	#print "RegMark:",RegMark
	if RegUserPwd == "":
		RegUserPwd = None

	if flag:
		print '修改成功'
		obj={'result':'t'}
	else:
		obj = {'result':'f','msg':'请稍后再试！'}
	code = str(json.dumps(obj))
	print code
	return HttpResponse(code)

def Advice(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	type=request.GET.get('type')
	username=request.session['username']
	print 'type=',type
	if type==None:
		print "none"
		type='SD'
	context = {'type':type,'username':username}
	advice_ = models.Advice()
	
	#advice_.send_advice(1,"没阅读啊哈哈","内容内容",1)
	#advice_.reply_advice(1,"回复回复",1,6)
	#参数如果没有就要写None作为占位符

	#timezone.now()
	
	
#timezone.now()
	return render(request, 'Member/Advice.html', context)
def AdviceSub(request):
	title=request.POST['title']
	info=request.POST['info']
	user_id=request.session['user_id']
	
	memobj=models.Member()
	advobj=models.Advice()
	service_id=memobj.myInfo(user_id).service_id
	print service_id
	print title
	print info
	flag=advobj.send_advice(user_id,title,info,service_id)
	print 'flag=',flag
	if flag:
		print "success"
		obj={'result':'t'}
	else:
		print "failed"
		obj = {'result':'f','msg':'请稍后再试！'}
	code = str(json.dumps(obj))
	print code
	return HttpResponse(code)

def AdviceList(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	user_id=request.session['user_id']
	username=request.session['username']
	title=request.GET.get('title')
	readstatus=request.GET.get('readstatus')
	start=request.GET.get('start')
	end=request.GET.get('end')
	advobj=models.Advice()
	print readstatus,start,end
	if readstatus=='':
		readstatus=None
		print 'service is none'
		
	if start=='':
		start=None
	if end=='':
		end=None
	if title == '':
		title=None
		print 'title is none'
	else:
		print title
	print "start:",start
	curpage = request.GET.get('p')
	if curpage == None:
			curpage='1';
	curpage=int(curpage)
	if curpage<=0:
		curpage=1
	print 'cur='+str(curpage)
	#my_advice(self,user_or_service_id_,role_="1",title_ = None,advice_status_ = None,\
       #           time_start_ = None,time_end_ = None,pageNum=1):
	advlist,pagenum,totalnum = advobj.my_advice(user_id,'1',title, readstatus,start,end,curpage)
	
	print pagenum,totalnum
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
		
	context = {
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
	
	context['username']=username
	context['title']=title
	context['readstatus']=readstatus
	context['start']=start
	context['end']=end
	context['advlist']=advlist
	for adv in advlist :
		print  adv.advice_title
	
	return render(request, 'Member/AdviceList.html', context)