#! /usr/bin/env python
# coding:utf-8
"""
红绿灯example,红灯,车子停,绿灯,车行!
event.clear() 代表清空标志位,代表红灯;
event.set() 代表设置标志位,代表绿灯;
thread 看见标志位才有有动作,否在wait;
"""

import time
import threading

event = threading.Event()

def lighter():
    """
    红灯,绿灯切换
    :return:
    """
    count = 0
    event.set() #默认位绿灯
    while True:
        if count > 5 and count < 10:  #红灯(亮10s),清空标志位
            lighter = event.clear()
            print("red")
        elif count > 10:
            event.set() #变成绿灯,设置标志位
            count = 0 #count 清零
        else:
            print("green")
            event.set()
        time.sleep(1)
        count += 1


def car(name):
    """
    车子行驶状态
    :param name: 车子的名字
    :return:
    """

    while True:
        if event.is_set():   #如果有标志位,代表是绿灯状态;
            print("[%s] running....." %name)
            time.sleep(1)
        else:            #没有标志位,代表是红灯状态;
            print("[%s] sees red light , waiting...." %name)
            event.wait()
            print("\033[34;1m[%s] green light is on, start going...\033[0m" %name)



light = threading.Thread(target=lighter)
light.start()
car1 = threading.Thread(target=car,args=('Tesla',))
car1.start()
