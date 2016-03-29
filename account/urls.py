from django.conf.urls import url,include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^login/$', views.login),
]
