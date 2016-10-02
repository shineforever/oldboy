#! /usr/bin/env python
# coding:utf-8
"""
ssh 上传和下载
"""
import paramiko

transport = paramiko.Transport(('127.0.0.1', 22))
transport.connect(username='root',password='vagrant')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/anaconda-ks.cfg', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
# sftp.get('remove_path', 'local_path')

transport.close()