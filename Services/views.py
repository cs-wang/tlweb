from django.shortcuts import render
from django.http import HttpResponse
from db import models
# Create your views here.

def DashBoard(request):
	context = {}
	return render(request, 'Services/DashBoard.html', context)

def NoticeList(request):
	context = {}
	return render(request, 'Services/NoticeList.html', context)

def MsgList(request):
	context = {}
	return render(request, 'Services/MsgList.html', context)

def MemberEdit(request):
	context = {}
#	 if request.method == 'GET':
#		 return 
#	 elif request.method == 'POST':
#		 return
	member_ = models.Member()
	flag = member_.register('wcs',"nickname_","delegation_phone_","delegation_info_",\
		  "bind_phone_","pwd","weixinId","bank_","account_","cardHolder","receiver_","reciever_phone_",\
		  "receiver_addr_","order_Memo",1,0)   
	return render(request, 'Services/MemberEdit.html', context)

def MemberList(request):
	context = {}
	return render(request, 'Services/MemberList.html', context)

def MemberOrder(request):
	context = {}
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