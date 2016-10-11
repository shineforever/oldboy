#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-10-11 14:06 
@author: guolt
"""

from django.http.response import HttpResponse

class Day13Middleware(object):
    """
    中间件测试
    """
    def process_request(self,request):
        print('1.process_request')
        # return HttpResponse('404')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('1.process_view')

    def process_exception(self, request, exception):
        print('1.process_exception')

    def process_response(self, request, response):
        print('1.process.process_reponse')
        return response

class Day13Middleware2(object):
    """
    中间件测试
    """
    def process_request(self,request):
        print('2.process_request')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('2.process_view')

    def process_exception(self, request, exception):
        print('2.process_exception')

    def process_response(self, request, response):
        print('2.process.process_reponse')
        return response

