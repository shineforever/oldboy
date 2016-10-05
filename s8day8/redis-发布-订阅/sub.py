#! /usr/bin/env python
# coding:utf-8

"""
redis 订阅端
"""

from redishelper import RedisHelper
import time

r=RedisHelper()
recv = r.subscribe()
while True:
    print(r.subscribe())