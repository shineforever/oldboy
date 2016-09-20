#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-09-19 17:44 
@author: guolt
"""

import MySQLdb
import conf

class MySqlHelper(object):
    """
    对mysql的操作
    """

    def __init__(self):
        self.__conn_dict = conf.conn_dic

    def Get_Dict(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        # cur = conn.cursor()  # 以元组形式展示产线的结果;((1L, 'python_change'), (3L, 'abc'), (4L, 'django'), (5L, 'django2'))
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)   #以字典形式显示搜索到得结果,所有列 ({'id': 1L, 'name': 'python_change'}, {'id': 3L, 'name': 'abc'}, {'id': 4L, 'name': 'django'})
        reCount = cur.execute(sql,params)
        data = cur.fetchall()
        cur.close()
        conn.close()

        return data

    def Get_One(self,sql,params):
        """
        获取一条参数
        :param sql:
        :param params:
        :return:
        """
        conn = MySQLdb.connect(**self.__conn_dict)  #字典形式
        # cur = conn.cursor()  # 以元组形式展示产线的结果;((1L, 'python_change'), (3L, 'abc'), (4L, 'django'), (5L, 'django2'))
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)   #以字典形式显示搜索到得结果,所有列 ({'id': 1L, 'name': 'python_change'}, {'id': 3L, 'name': 'abc'}, {'id': 4L, 'name': 'django'})
        reCount = cur.execute(sql,params)
        data = cur.fetchone()
        cur.close()
        conn.close()

        return data


if __name__ == '__main__':
    helper = MySqlHelper()
    sql = "select * from admin WHERE id = %s"
    params = (1,)
    result =  helper.Get_One(sql,params)
    print result
