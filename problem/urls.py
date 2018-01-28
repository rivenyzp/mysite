#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:RivenYzp

from django.conf.urls import patterns,url
from problem import views

urlpatterns = patterns('',
    url(r'^problem_show/',views.problem_show,name='problem_show'),
    url(r'^problem_show_one/',views.problem_show_one,name='problem_show_one'),
    url(r'^problem_isRight/',views.problem_isRight,name='problem_isRight'),
    # ([A-Za-z0-9]+)$/$ //匹配数字加英文的正则表达式
)