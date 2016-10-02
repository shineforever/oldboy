#! /usr/bin/env python
# coding:utf-8

"""
python 队列example,标准库中queue
"""

import Queue

q=Queue.Queue()

#依次放入数据,默认是先进先出:
q.put(2)
q.put(3)
q.put(5)

#取出队列
print(q.get())
print(q.get())
print(q.get())

################
#先进后出
################
q=Queue.LifoQueue()   #Last in First Out!

#依次放入数据,默认是先进先出:
q.put(2)
q.put(3)
q.put(5)

#取出队列
print(q.get())
print(q.get())
print(q.get())