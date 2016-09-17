#! /usr/bin/env python
# coding:utf-8

import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='s8day5')
cur = conn.cursor()


sql = "insert into userinfo(name) values(%s)"  #insert
parms = ('python_change',)

reCount = cur.execute(sql,parms)
#select,insert.delete操作都需要加上commit!!!
conn.commit()

cur.close()
conn.close()

print reCount
