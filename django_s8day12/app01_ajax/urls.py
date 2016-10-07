#! /usr/bin/env python
# coding:utf-8

from django.conf.urls import patterns, include, url
from app01_ajax import views


urlpatterns = [
    url(r'^index/$', views.index),
]