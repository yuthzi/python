# -*- coding: UTF-8 -*- 
'''
Created on 2017年10月5日

@author: Administrator
'''

from urllib import quote
import requests

def sendByGet(sUrl):
    header = {}
    try:
        response=requests.get(sUrl, headers=header)
        sText = response.text
        return sText
    except BaseException:
        print BaseException
            
def demo(msg):
    sEncodeMsg = quote(msg.encode('utf-8'))
    url = 'http://www.youdao.com/w/eng/' + sEncodeMsg
    print sendByGet(url)
    
demo(u'数据')    