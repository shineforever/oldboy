#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-10-10 15:17 
@author: guolt
"""

from django.conf.urls import patterns, include, url
from account import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^login_after/$', views.login_after),
]