#! /usr/bin/env python
# coding:utf-8

"""
redis 发布端
"""

from redishelper import RedisHelper
import time

r=RedisHelper()
r.pub("this msg from pub server")

# while True:
#     r.pub("this msg from pub server")
#     time.sleep(1)