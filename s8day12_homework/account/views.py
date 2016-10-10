#! /usr/bin/env python
# coding: utf-8
from django.shortcuts import render,render_to_response,HttpResponse,redirect
from models import *
import json


# Create your views here.


def index(request):
    return HttpResponse('index page!!!')

def login(request):
    """
    login
    :param request:
    :return:
    """
    # return HttpResponse('login page!!!')
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        # print(username,password)
        if username == 'abc'and password == 'abc':
            # pass
            request.session['is_login'] = {'user':username}   #设置session
            return redirect('/account/login_after')    #重定向到另外一个页面
        else:
            print(request.session)
            return render_to_response('account/login.html',{'msg':'用户名或者密码错误！'})
    else:
        return render_to_response('account/login.html')

def login_after(request):
    user_dict = request.session.get('is_login',None)
    if user_dict:
        return render_to_response('account/login_after.html',{'username':user_dict['user']})
    else:
        return redirect('index.html')

def logout(request):
    """
    用户注册,其实就是删除sess和重定向到指定页面的过程；
    :param request:
    :return:
    """
    del request.session['is_login']
    return redirect('/account/login/')