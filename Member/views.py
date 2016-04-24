# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.db import transaction
from django.utils.dateparse import parse_datetime
from cStringIO import StringIO
import qrcode
import pytz
# Create your views here.
import json
from db import models
from urllib2 import Request

site_dns = 'http://192.168.3.108:8000'


def DashBoard(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	context = {}
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
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	context = {}
	return render(request, 'Member/MsgList.html', context)

def ShowModel(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	user_id = int(request.session['user_id']) 
	user = models.Member().getUser(user_id)
	global site_dns
	context = {'reference_id':0}
	if user!= None:
		context['reference_id'] = reference_id 
	return render(request, 'Member/ShowModel.html', context)

def ComBank(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	context = {}
	return render(request, 'Member/ComBank.html', context)

def MemberOrder(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	member_ = models.OrderForm()
	ordlist, maxPage = member_.myMemberOrder(1,None,None,"1",1)
	for i in ordlist:
		print i.order_id
	print "最多",maxPage
	
	context = {}
	return render(request, 'Member/MemberOrder.html', context)

def RewardOrder(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	context = {}
	return render(request, 'Member/RewardOrder.html', context)

def RewardOrderList(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	context = {}
	return render(request, 'Member/RewardOrderList.html', context)
@transaction.atomic
def Recome(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	context = {}
	return render(request, 'Member/Recome.html', context)

def RecomeList(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	context = {}
	return render(request, 'Member/RecomeList.html', context)

def MyRecomeAll(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	context = {}
	member_ = models.Member()
	list ,maxPage = member_.myReference(1,1)
	print list
	print "最多",maxPage
	return render(request, 'Member/MyRecomeAll.html', context)

def MyData(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	context = {}
	return render(request, 'Member/MyData.html', context)

def Advice(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	context = {}
	advice_ = models.Advice()
	#advice_.send_advice(1,"没阅读啊哈哈","内容内容",1)
	#advice_.reply_advice(1,"回复回复",1,6)
	#参数如果没有就要写None作为占位符

	#timezone.now()
	
	
#timezone.now()
	return render(request, 'Member/Advice.html', context)

def AdviceList(request):
	if request.session['role'] != '0':
		return HttpResponseRedirect('/')
	context = {}
	advice_ = models.Advice()
	naive = parse_datetime("2016-03-21 10:28:45")
	time_ = pytz.timezone("UTC").localize(naive, is_dst=None)	
	adlist,maxPage =  advice_.my_advice(1,"0",None,None,time_,timezone.now())
	for i in adlist :
		print i.advice_id
	print "最多",maxPage
	return render(request, 'Member/AdviceList.html', context)

def QrCode(request, ReferenceId):
	global dns_site
	url = site_dns + "/Account/Reg/" + str(ReferenceId)+"/"
	print url
	img = qrcode.make(url);
	buf = StringIO()
  	img.save(buf)
  	image_stream = buf.getvalue()
	return HttpResponse(image_stream , content_type="image/png")