#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月2日

@author: Administrator
'''
import logging

# ref: http://blog.csdn.net/dezhihuang/article/details/72122356

# define the log file, file mode and logging level
logging.basicConfig(filename='example.log', filemode="w", level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

# 新建一个logger
myLogger = logging.getLogger('simple_example')
try:  
    fh = logging.FileHandler("my.log")  
    fh.setLevel(logging.DEBUG)  
    myLogger.addHandler(fh)  
    myLogger.info('So should this')  
except Exception as e:  
    print e  

myLogger.warning('myLogger')




