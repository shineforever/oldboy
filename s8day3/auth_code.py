#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-08-23 07:57 
@author: guolt
"""

import random

code = []
for i in range(6):
    if i == random.randint(1,6):
        code.append(str(i))
    else:
        temp = random.randrange(65,90)
        code.append(chr(temp))

print code   #列表形式的验证码
print "".join(code)  #列表转化为字符串




