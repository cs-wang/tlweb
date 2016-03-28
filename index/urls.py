from django.conf.urls import url,include
from django.contrib import admin
import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^/company$', views.company),
    url(r'^/product$', views.product),
]
