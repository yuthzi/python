# -*- coding: UTF-8 -*- 
'''
Created on 2017年10月1日

@author: Administrator
'''
def demo():
    try:
        fh = open("test.txt", "w")
        fh.write("这是一个测试文件，用于测试异常!!")
    except EOFError:
        print "EOFError: 没有找到文件或读取文件失败"
    except IOError:
        print "Error: 没有找到文件或读取文件失败"
    else:
        print "内容写入文件成功"
    finally:
        fh.close()


if __name__ == '__main__':
    demo()
