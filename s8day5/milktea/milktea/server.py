#!/usr/bin/env python
#coding:utf-8


import SocketServer
import json
import time
from backend.models import UserInfo,ChatRecord

class  MyServer(SocketServer.BaseRequestHandler):
    
    def setup(self):
        pass

    def handle(self):
        userinfo = UserInfo() #实例化一个用户表操作类
        chatrecord = ChatRecord() #实例化一个记录表操作类
        
        container = {'key':'','data':''}
        container['data'] = 'ok...'
        
        conn = self.request
        conn.sendall(json.dumps(container))
        Flag = True
        while Flag:
            try:
                data = conn.recv(1024)
                print data
                rev_data = json.loads(data)
                if rev_data['data'] == 'exit':
                    conn.close()
                    break
                #如果key为空，则表示用户没有登录或登录失败
                if not rev_data['key']:
                    name,pwd = rev_data['data']
                    re = userinfo.CheckLogin(name, pwd)
                    # re = 1
                    if re:
                        rev_data['key'] = re
                        rev_data['data'] = '约吗？'
                    else:
                        rev_data['data'] = 'failed.'
                    conn.sendall(json.dumps(rev_data))
                #用户已经登录
                else:
                    datetime = time.strftime('%Y-%m-%d %H:%M:%S')
                    
                    if rev_data['data']=='list': #聊天记录
                        rev_data['data'] = chatrecord.GetRecord(rev_data['key'])
                        pass
                        
                    elif rev_data['data'].__contains__('yes'): 
                        #如果用户输入的是yes，那么就把用户输入的记录保存到数据
                        chatrecord.InsertRecord(rev_data['data'], datetime, rev_data['key'])
                        rev_data['data'] = 'I am gay.'
                        #把聊天机器人的回复也保存到数据库
                        chatrecord.InsertRecord(rev_data['data'], datetime, rev_data['key'])
                    else: 
                        #如果用户输入的不是yes,把用户输入的记录保存到数据
                        chatrecord.InsertRecord(rev_data['data'], datetime, rev_data['key'])
                        rev_data['data'] = 'what?'
                        #把聊天机器人的回复也保存到数据库
                        chatrecord.InsertRecord(rev_data['data'], datetime, rev_data['key'])
                    conn.sendall(json.dumps(rev_data))
            except Exception,e:
                print e
                Flag = False
    def finish(self):
        pass
        
if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',9998),MyServer)
    server.serve_forever()