#! /usr/bin/env python
# coding: utf-8
"""
类的反射 example account/login or account/logout
"""

data = raw_input("please input your url: ")
data_lst=data.split("/")
str="backend."+data_lst[0]

try:
    userspace=__import__(str)  #导入backend.account文件夹
    model=getattr(userspace,data_lst[0]) # 导入account的类
    func=getattr(model,data_lst[1])    #从account类中找到相对应得方法;
    func()
except:
    print "error"
