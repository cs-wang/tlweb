from django.conf.urls import url,include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^DashBoard/$', views.DashBoard),
    url(r'^MsgList/$', views.MsgList),
    url(r'^ShowModel/$', views.ShowModel),
    url(r'^ComBank/$', views.ComBank),
    url(r'^MemberOrder/$', views.MemberOrder),
    url(r'^RewardOrder/$', views.RewardOrder),
    url(r'^RewardOrderList/$', views.RewardOrderList),
    url(r'^Recome/$', views.Recome),
    url(r'^RecomeList/$', views.RecomeList),
    url(r'^MyRecomeAll/$', views.MyRecomeAll),
    url(r'^MyData/$', views.MyData),
    url(r'^Advice/$', views.Advice),
    url(r'^AdviceList/$', views.AdviceList),
]
