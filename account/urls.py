from django.conf.urls import url,include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve',{'document_root':'./assets'}),
    url(r'^login/$', views.login)
]
