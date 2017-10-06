#-*- coding: UTF-8 -*-
'''
Created on 2017年10月6日

@author: Administrator
'''

import datetime

t1 = datetime.datetime.strptime("2017-9-06 10:30:00", "%Y-%m-%d %H:%M:%S")
t2 = datetime.datetime.strptime("2017-9-06 12:30:00", "%Y-%m-%d %H:%M:%S")

interval_time = (t2 - t1).seconds  # 输入的结果：7200
total_interval_time = (t2 - t1).total_seconds() # 输出结果是: 7200.0
print interval_time
print total_interval_time

# 换一个方式
t1 = datetime.datetime.strptime("2017-9-06 10:30:00", "%Y-%m-%d %H:%M:%S")
t2 = datetime.datetime.strptime("2017-9-08 12:30:00", "%Y-%m-%d %H:%M:%S")
interval_time = (t2 - t1).seconds  # 输入的结果：7200
total_interval_time = (t2 - t1).total_seconds() # 输出结果是: 180000.0
print interval_time
print total_interval_time
td = (t2 - t1)
print((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6)

# datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
td = datetime.timedelta(6, 5, 1, 800, 12, 3) 
print td # 6 days, 3:12:05.800001
print td.seconds # 11525 忽略微秒和天
print td.total_seconds() # 529925.800001

