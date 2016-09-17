#! /usr/bin/env python
# coding:utf-8

import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='s8day5')
# cur = conn.cursor()  # 以元组形式展示产线的结果;((1L, 'python_change'), (3L, 'abc'), (4L, 'django'), (5L, 'django2'))
cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)   #以字典形式显示搜索到得结果,所有列 ({'id': 1L, 'name': 'python_change'}, {'id': 3L, 'name': 'abc'}, {'id': 4L, 'name': 'django'})



sql = "select * from userinfo"  #select
reCount = cur.execute(sql)
data = cur.fetchone()
print data

data = cur.fetchone()
print data

data = cur.fetchone()
print data


cur.close()
conn.close()

print reCount
