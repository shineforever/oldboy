#! /usr/bin/env python
# coding: utf-8

def outer(func):
    def wrapper():
        print "before func"
        func()
        print "after func"
    return wrapper
       


@outer
def func1():
    print "func1"

@outer
def func2():
    print "func2"

@outer
def func3():
    print "func3"



func1()
func2()
func3()
