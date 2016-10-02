#! /usr/bin/env python
# coding:utf-8

"""
多线程执行完成后,计算多线程执行消耗时间,在thread中wait就是join
"""

import threading
import time

def run(n):
    print("task: ",n,threading.current_thread())  #查看每个thread的id
    time.sleep(2)


start_time = time.time()

t_objs=[]
for i in range(50):
    t = threading.Thread(target=run,args=("t: %s" %i,))
    t.start()
    t_objs.append(t)    #把进程加入到一个list中;

#等待所有的进程全部执行完成
for i in t_objs:
    i.join()

#计算时间
print("all thread had finished.....", threading.current_thread())
print("cost: ", time.time() - start_time)