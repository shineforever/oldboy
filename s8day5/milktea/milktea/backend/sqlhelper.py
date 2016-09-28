#!/usr/bin/env python
#coding:utf-8

import MySQLdb
import _mysql_exceptions

class MySqlHelper:
    
    def __init__(self):
        self.__connDict = {'host':'192.168.2.42','user':'root','passwd':'123456','port':33066,'db':'milkteadb'}
        
        
    def GetSimple(self,sql,params):
        '''获取单条数据
        @param sql:sql语句
        @param params:参数
        @return: 数据  
        '''
        conn = MySQLdb.connect(**self.__connDict)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        cur.execute(sql,params)
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data
    
    def GetDict(self,sql,params):
        '''获取多条数据（字典类型）'''
        conn = MySQLdb.connect(**self.__connDict)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        cur.execute(sql,params)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    
    def InsSample(self,sql,params):
        '''插入单条数据
        @return: 受影响的条数
        '''
        conn = MySQLdb.connect(**self.__connDict)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        count = cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
        return count
    
    def InsSample_ReturnId(self,sql,params):
        '''插入单条数据
        @return: 返回自增ID
        '''
        conn = MySQLdb.connect(**self.__connDict)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        cur.execute(sql,params)
        id = cur.lastrowid
        conn.commit()
        cur.close()
        conn.close()
        return id
        