#! /usr/bin/env python
# coding: utf-8

from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = '用户类型'            #点击admin首页相关字段进去后的页面显示，例如：
        verbose_name_plural = "用户类型"    #admin后台首页字段汉字显示；

class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    user_type = models.ForeignKey('UserType')

class UserGroup(models.Model):
    groupname = models.CharField(max_length=50)
    user = models.ManyToManyField('UserInfo')

class Asset(models.Model):
    hostname = models.CharField(max_length=256)
    ip = models.GenericIPAddressField()
    location = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add = True)
    user_group = models.ForeignKey('UserGroup')