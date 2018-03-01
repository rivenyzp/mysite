#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:RivenYzp

from django.conf.urls import patterns, url
from login import views

urlpatterns = patterns('',
                       # url(r'^$', views.login, name='login'),
                       url(r'^login/$', views.login, name='login'),
                       url(r'^register/$', views.is_register, name='register'),
                       url(r'^register_to/$', views.register, name='register_to'),
                       url(r'^login_to/$',views.login_to,name='login_to'),
                       url(r'^index/$',views.index,name='index'),
                       url(r'^login_out/$',views.login_out,name='login_out'),
                       url(r'^home/$',views.home,name='home'),
                       #url(r'^index/$', views.index, name='index'),
                       #url(r'^logout/$', views.logout, name='logout'),
                       )