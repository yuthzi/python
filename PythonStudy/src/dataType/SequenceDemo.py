#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月5日

@author: Administrator
'''

# 这是编译时的字符串连接。使用加号是运行时的字符串连接
a = ('http://' # protocol
    'localhost'# hostname
    ':8000' # port
    '/demo/test.py') # file
  
print a  


