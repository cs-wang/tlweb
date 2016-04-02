from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def DashBoard(request):
	context = {}
	return render(request, 'Member/DashBoard.html', context)

def MsgList(request):
	context = {}
	return render(request, 'Member/MsgList.html', context)

def ShowModel(request):
	context = {}
	return render(request, 'Member/ShowModel.html', context)

def ComBank(request):
	context = {}
	return render(request, 'Member/ComBank.html', context)

def MemberOrder(request):
	context = {}
	return render(request, 'Member/MemberOrder.html', context)

def RewardOrder(request):
	context = {}
	return render(request, 'Member/RewardOrder.html', context)

def RewardOrderList(request):
	context = {}
	return render(request, 'Member/RewardOrderList.html', context)

def Recome(request):
	context = {}
	return render(request, 'Member/Recome.html', context)

def RecomeList(request):
	context = {}
	return render(request, 'Member/RecomeList.html', context)

def MyRecomeAll(request):
	context = {}
	return render(request, 'Member/MyRecomeAll.html', context)

def MyData(request):
	context = {}
	return render(request, 'Member/MyData.html', context)

def Advice(request):
	context = {}
	return render(request, 'Member/Advice.html', context)

def AdviceList(request):
	context = {}
	return render(request, 'Member/AdviceList.html', context)