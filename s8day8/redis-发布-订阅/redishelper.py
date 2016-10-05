#! /usr/bin/env python
# coding:utf-8

import redis

class RedisHelper(object):
    """
    redis 连接
    """
    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1',port=6379,db=0,password=123456)
        self.chan_pub = 'channel_demo'   #发布消息的channel
        self.chan_sub = 'channel_demo'   #订阅消息的channel

    def get(self,key):
        """
        获取key值
        :param key:
        :return:
        """
        return self.__conn.get(key)

    def set(self,key,value):
        """
        设置key值
        :param key:
        :param value:
        :return:
        """
        self.__conn.set(key,value)

    def pub(self,msg):
        """
        发布消息到redis
        :return:
        """
        self.__conn.publish(channel=self.chan_pub,message=msg)
        return True

    def subscribe(self):
        """
        订阅指定频道的消息
        :return:
        """
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()    #开始等待消息
        return pub



if __name__ == '__main__':
    t = RedisHelper()
    t.pub('msg from redis!!!')   #发布消息