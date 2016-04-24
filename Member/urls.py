from django.conf.urls import url,include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^DashBoard/$', views.DashBoard),
    url(r'^DashBoard/ReConsume/$', views.ReConsume),
    url(r'^DashBoard/ReConsume/ReConsumeSave/$', views.ReConsumeSave),
    url(r'^MsgList/ViewMsg/$',views.ViewMsg),
   url(r'^MsgList/ViewMsg/MsgRead/$', views.MsgRead),
    url(r'^MsgList/$', views.MsgList),
    url(r'^ShowModel/$', views.ShowModel),
    url(r'^ComBank/$', views.ComBank),
    url(r'^MemberOrder/$', views.MemberOrder),
    url(r'^RewardOrder/$', views.RewardOrder),
    url(r'^RewardOrderList/$', views.RewardOrderList),
    url(r'^Recome/$', views.Recome),
    url(r'^Recome/RecomeSave/$',views.RecomeSave),
    url(r'^RecomeList/$', views.RecomeList),
    url(r'^MyRecomeAll/$', views.MyRecomeAll),
    url(r'^MyData/MyDataUpdate/$',views.MyDataUpdate),
    url(r'^MyData/$', views.MyData),
    url(r'^Advice/AdviceSub/$',views.AdviceSub),
    url(r'^UserMap/GetMap/$',views.GetMap),
    url(r'^UserMap/$',views.UserMap),
    url(r'^Advice/$', views.Advice),
    url(r'^AdviceList/$', views.AdviceList),
     url(r'^AdviceList/AdviceView/$', views.AdviceView),
    url(r'^QrCode/(?P<ReferenceId>(\d)*)/$', views.QrCode)
]
