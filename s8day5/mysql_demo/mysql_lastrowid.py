#! /usr/bin/env python
# coding:utf-8

"""
获得insert成功后的id值,一般用于上传资源到服务器后,获得id与其他资源结合;
"""

import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='s8day5')
cur = conn.cursor()


sql = "insert into userinfo(name) values(%s)"  #insert
parms = ('python_abc',)
reCount = cur.execute(sql,parms)
#select,insert.delete操作都需要加上commit!!!
conn.commit()

print "获得 insert 成功后的自增id %s" % cur.lastrowid

cur.close()
conn.close()



