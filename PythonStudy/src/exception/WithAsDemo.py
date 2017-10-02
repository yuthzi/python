# -*- coding: UTF-8 -*- 
'''
Created on 2017年10月1日

@author: Administrator
'''
def demo():
    with open('test.txt', 'r') as f:
        f.read()
        print 2 / 0
        print 'continue'

if __name__ == '__main__':
    demo()
