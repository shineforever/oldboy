#! /usr/bin/env python
# coding: utf-8
from django.shortcuts import render,render_to_response,HttpResponse,redirect
from django.template import RequestContext  #使用csrf功能时要import
from django.views.decorators.csrf import csrf_exempt #引用不需要csrf认证的装饰器
from models import *
import json


# Create your views here.


def index(request):
    print('index page')
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
        is_check = UserInfo.objects.filter(username=username,password=password).count()
        if is_check:
            # pass
            request.session['is_login'] = {'user':username}   #设置session
            return redirect('/account/login_after')    #重定向到另外一个页面
        else:
            print(request.session)
            return render_to_response('account/login.html',{'msg':'用户名或者密码错误！'},context_instance=RequestContext(request))
    else:
        return render_to_response('account/login.html',context_instance=RequestContext(request))

@csrf_exempt
def login_no_csrf(request):
    """
    不使用csrf
    :param request:
    :return:
    """
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