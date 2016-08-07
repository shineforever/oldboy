#! /usr/bin/env python
# coding:utf-8

"""
s8day9 作业,文本替换
"""

import sys,os

if len(sys.argv) < 4:
    print('Usage: file_replace.py oldstring newstring filename --bak')
else:
    #file_replace.py oldstring newstring filename
    filename = sys.argv[3]
    oldstring,newstring = sys.argv[1],sys.argv[2]
    f=file(filename,'rb')
    tmp_file = file('.%s.tmp' % filename,'wb')

    for line in f.xreadlines():
        tmp_file.write(line.replace(oldstring,newstring))
    f.close()
    tmp_file.close()

    if '--bak' not in sys.argv:
        os.rename('.%s.tmp' %filename,filename)
    else:
        os.rename(filename,'%s.bak' % filename)  #重命名原文件为 .bak结尾
        os.rename('.%s.tmp' %filename,filename)





