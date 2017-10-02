# -*- coding: UTF-8 -*- 
'''
Created on 2017年10月1日

@author: Administrator
'''
import traceback


def deliverExc(exp):
    '''
          捕捉到异常之后往上传递
    '''
    try:
        return eval(exp)
    # except ZeroDivisionError:
    except(ZeroDivisionError, RuntimeError) :
        print("occour a ZeroDivisionError when eval exp")
        traceback.print_exc() # 打印异常堆栈信息
        #pass
        #raise

print deliverExc("2 / 0")
print deliverExc("2 / 1")
