#! /usr/bin/env python
# coding:utf-8


import sys,os

if len(sys.argv) < 4:
    print('Usage: file_replace.py oldstring newstring filename --bak')
else:
    #file_replace.py oldstring newstring filename
    filename = sys.argv[3]
    oldstring,newstring = sys.argv[1],sys.argv[2]
    file=os.open(filename,'rb')
    tmp_file = file('.%s.tmp' % filename,'wb')

    for line in file.xreadlines():
        tmp_file.write(line.replace(oldstring,newstring))
    file.close()
    tmp_file.close()

