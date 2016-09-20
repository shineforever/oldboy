#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-09-19 17:47 
@author: guolt
数据库中一张表，对应一个py文件
"""

# import sys
# sys.path.append('/coding/oldboy/s8day5_mysql')
"""
如果在model目录下执行 admin文件，就需要上面的两行，把文件的更目录加到python的环境变量中；如果是直接在目录的根目录执行文件，然后调用 model/admin，model/admin再调用utility/sql_helper 就不需要上面两行
"""

from utility.sql_helper import MySqlHelper

#sys.path.append('/coding/oldboy/s8day5_mysql')
# print sys.path


class Admin(object):

    def __init__(self):
        self.__helper = MySqlHelper()

    def Get_One(self,id):
        sql = "select * from admin WHERE id = %s"
        params = (id,)
        result = self.__helper.Get_One(sql,params)
        return result

    def ValidLogin(self,username,password):
        """
        用户登录验证
        :param username:
        :param password:
        :return:
        """
        sql = "select * from admin WHERE name=%s AND password=%s"
        params = (username,password)
        result = self.__helper.Get_One(sql,params)
        return result


if __name__ == '__main__':
    mysql_admin = Admin()
    print mysql_admin.Get_One(1,)

