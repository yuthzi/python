# -*- coding: UTF-8 -*- 
'''
Created on 2017年10月1日

@author: Administrator
'''
# raise语法格式如下：
# raise [Exception [, args [, traceback]]]

def throwExc(number):
    '''
        抛出异常
    '''
    raise Exception(u"抛出一个异常", number) #异常被抛出，print函数无法执行
    print("yuthzi")
    
if __name__ == '__main__':
    throwExc(0)