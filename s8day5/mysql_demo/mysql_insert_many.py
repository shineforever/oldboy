#! /usr/bin/env python
# coding:utf-8

import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='s8day5')
cur = conn.cursor()


sql = "insert into userinfo(name) values(%s)"  #insert

parms_many = [
    ('abc1',),
    ('abc2',),
    ('abc3',)

]
# reCount = cur.execute(sql,parms)
manyCount=cur.executemany(sql,parms_many)   #链接一次数据库,insert多条数据,然后commit!

#select,insert.delete操作都需要加上commit!!!
conn.commit()

cur.close()
conn.close()

print manyCount