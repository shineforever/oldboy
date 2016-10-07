#! /usr/bin/env python
# coding:utf-8

from django.shortcuts import render,render_to_response,HttpResponse
# from django.http.response import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("ajax test page!!!")