from django.conf.urls import url,include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^anounce/$', views.anounce),
    url(r'^message/$', views.message),
    url(r'^register/$', views.register),
]
