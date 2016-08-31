#! /usr/bin/env python
# coding:utf-8

"""
Created on: 2016-08-31 08:40 
@author: guolt
"""

class Province(object):

    memo="静态字段"

    def __init__(self,name,captical,leader,flag):
        self.Name = name
        self.Captical = captical
        self.Leader = leader
        self.__abc = flag

    #动态方法
    def bar(self):
        print "Bar"

    def show(self):
        print self.__abc

    @staticmethod     #静态方法,不需要传参数 self
    def Foo():
        print "静态方法,不需要实例化后使用"

    @property  #把动态的方法转化为特殊静态字段
    def static(self):
        print self.__abc


hb=Province('湖北','武汉','abc',True)
hb.bar()

#内部调用使用方法
hb.show()

print "打印静态字段： " + Province.memo

#特殊字段调用
hb.static

#静态方法调用
Province.Foo()