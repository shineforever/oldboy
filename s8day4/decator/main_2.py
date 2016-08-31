#! /usr/bin/env python
# coding: utf-8

"""
带参数的装饰器
"""

def outer(func):
    def wrapper(arg):
        print "before func"
        func(arg)
        print "after func"
    return wrapper
       


@outer
def func1(arg):
    print "func1",arg





func1('pyabc')
