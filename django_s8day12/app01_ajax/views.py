#! /usr/bin/env python
# coding:utf-8

from django.shortcuts import render,render_to_response,HttpResponse
# from django.http.response import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        print request.POST
        return HttpResponse("msg from ajax server")
    else:
        return render_to_response('app01/ajax.html')