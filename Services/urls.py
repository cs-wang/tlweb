from django.conf.urls import url,include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^DashBoard/$', views.DashBoard),
    url(r'^NoticeList/$', views.NoticeList),
    url(r'^MsgList/$', views.MsgList),
    url(r'^MsgList/ViewMsg/$', views.ViewMsg),
    url(r'^MsgList/ViewMsg/MsgRead/$', views.MsgRead),
    url(r'^MemberEdit/$', views.MemberEdit),
    url(r'^MemberList/$', views.MemberList),
    url(r'^MemberList/SetAudit/$', views.SetAudit),
    url(r'^MemberList/MemberEdit/$', views.MemberEdit),
    url(r'^MemberOrder/$', views.MemberOrder),
    url(r'^UserMap/$', views.UserMap),
    url(r'^ComBank/$', views.ComBank),
    url(r'^Promotion/$', views.Promotion),
    url(r'^AdviceList/$', views.AdviceList),
    url(r'^AdviceList/AdviceView/$', views.AdviceView),
    url(r'^AdviceList/AdviceView/AdviceSub/$', views.AdviceSub),
    url(r'^SubService/$', views.SubService),
]
