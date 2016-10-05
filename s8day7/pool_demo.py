#! /usr/bin/env python
# coding:utf-8

"""
多进程demo

result:
没有使用多进程的情况:
[1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]
total time: 5.00897502899
####################
使用多进程:
[1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]
total time: 1.05102586746
"""

from multiprocessing import Pool
import time

a = range(10)

def f(n):
    time.sleep(0.5)
    return n**n


if __name__ == '__main__':
    print("没有使用多进程的情况: ")
    start_time = time.time()
    print(map(f,a))
    print("total time: %s" %(time.time()-start_time))

    print('#'*20)
    print("使用多进程: ")
    start_time = time.time()
    p=Pool(5)
    print(p.map(f,a))
    print("total time: %s" %(time.time()-start_time))

