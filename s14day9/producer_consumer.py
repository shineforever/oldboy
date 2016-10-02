#! /usr/bin/env python
# coding:utf-8

"""
利用队列实现生产,消费者模型
"""

import threading
import Queue

q = Queue.Queue()

def producer():
    for i in range(10):
        q.put("骨头: %s" %i)


def concumer(name):
    while q.qsize() > 0:
        print("%s get: %s" %(name,q.get()))


producer1 = threading.Thread(target=producer,)
producer1.start()

consumer1 = threading.Thread(target=concumer,args=("someone",))
consumer1.start()