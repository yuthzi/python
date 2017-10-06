#-*- coding: UTF-8 -*-
'''
Created on 2017年10月6日

@author: Administrator
'''

from datetime import datetime

'''
测试多种字符串连接的速度。似乎相差不大？
str1 = ('0yuth'
        '1yuth'
        '2yuth')

str2 = ('0yuth' +
        '1yuth' +
        '2yuth')

str3 = '0yuth' + \
       '1yuth' + \
       '2yuth'

str4 = '0yuth' +  '1yuth' +  '2yuth'
str5 = '0yuth' '1yuth' '2yuth'
'''

iTimes = 1000000

def concatStr0():
    startTime = datetime.now()
    str0 = '0yuth1yuth2yuth'
    for i in range(0,iTimes):
        str0 #+ str(i)
        s = str0
    print "\t\t\t" + s  
    endTime = datetime.now()
    print (endTime-startTime).microseconds
    #print (endTime-startTime).total_seconds()
        
def concatStr1():
    startTime = datetime.now()
    for i in range(0,iTimes):
        str1 = ('0yuth'
            '1yuth'
            '2yuth') #+ str(i)
        s = str1
    print "\t\t\t" + s
    endTime = datetime.now()
    print (endTime-startTime).microseconds
    #print (endTime-startTime).total_seconds()

def concatStr2():
    startTime = datetime.now()
    for i in range(0,iTimes):
        str2 = ('0yuth' +
        '1yuth' +
        '2yuth')  #+ str(i)
        s = str2
    print "\t\t\t" + s
    endTime = datetime.now()
    print (endTime-startTime).microseconds
    #print (endTime-startTime).total_seconds()
   
def concatStr3():
    startTime = datetime.now()
    for i in range(0,iTimes):
        str3 = '0yuth' + \
                '1yuth' + \
                '2yuth' #+ str(i)
        s = str3
    print "\t\t\t" + s
    endTime = datetime.now()
    print (endTime-startTime).microseconds
    #print (endTime-startTime).total_seconds()    
    
   
def concatStr4():
    startTime = datetime.now()
    for i in range(0,iTimes):
        str4 = '0yuth' +  '1yuth' +  '2yuth'  #+ str(i)
        s = str4
    print "\t\t\t" + s
    endTime = datetime.now()
    print (endTime-startTime).microseconds
    #print (endTime-startTime).total_seconds()     

def concatStr5():
    startTime = datetime.now()
    for i in range(0,iTimes):
        str5 = '0yuth' '1yuth' '2yuth' # + str(i)
        s = str5
    print "\t\t\t" + s
    endTime = datetime.now()
    print (endTime-startTime).microseconds
    #print (endTime-startTime).total_seconds()        
 
def test():  
    concatStr0()  
    concatStr1()
    concatStr2()
    concatStr3()
    concatStr4()
    concatStr5()
      
if __name__ == '__main__':  
    test()

