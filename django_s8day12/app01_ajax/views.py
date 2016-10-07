#! /usr/bin/env python
# coding:utf-8

from django.shortcuts import render,render_to_response,HttpResponse
import json

# Create your views here.

def index(request):
    if request.method == 'POST':
        print request.POST
        data = {'status':0,'msg':'请求成功','data':[111,3333,5555]}
        return HttpResponse(json.dumps(data))
        # return HttpResponse("msg from ajax server")
    else:
        return render_to_response('app01/ajax.html')