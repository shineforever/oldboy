#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-08-08 16:26 
@author: guolt
找到一个文本中符合条件的行，关键字高亮
"""

import sys

f = file('passwd.txt','rb')

match_flag = 0
search_key = raw_input('please input your search key: ')
for line in f.xreadlines():
    if search_key in line:
        match_flag += 1
        color_search_key = "\033[41;36m%s\033[0m" % search_key
        print line.replace(search_key,color_search_key)

print "have %s line match your search!!! " % match_flag
# print "\033[41;36m something here \033[0m"



