#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-09-19 09:18 
@author: guolt
"""

from model.admin import Admin


def main():
    user = raw_input("username: ")
    passwd = raw_input("password: ")
    check_login = Admin()
    result = check_login.ValidLogin(user,passwd)
    if not result:
        print "user or passwd is wrong!"
    else:
        print "login success!"


if __name__ == "__main__":
    main()

