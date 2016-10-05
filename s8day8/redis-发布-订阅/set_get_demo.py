#! /usr/bin/env python
# coding:utf-8

"""
在redis设置一个key,然后去获取他得值
"""

from redishelper import RedisHelper

r = RedisHelper()
# 设置key
r.set('name','wweeee2222')

# 获取key
print(r.get('name'))
