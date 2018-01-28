#-*- coding: UTF-8 -*-
'''
Created on 2017年10月14日

@author: Administrator
'''
import pyaudio
import wave  
import time 

'''
pyaudio使用例子。
PyAudio 是语音处理的 Python 库，提供了比较丰富的功能。
具体功能如下：
特征提取(feature extraction)：关于时域信号和频域信号都有所涉及
分类(classification)：监督学习，需要用已有的训练集来进行训练。交叉验证也实现了，进行参数优化使用。分类器可以保存在文件中以后使用。
回归(regression)：将语音信号映射到一个回归值。
分割(segmenttation)：有四个功能被实现了
[x] 固定大小的分割
[x] 静音检测（silence removal）
[x] 语音聚类（speaker diarization）
[x] 语音缩略图(audio thumbnailing)
可视化：给定语音，将内容可视化[1] 
'''

def play():
    #定义数据流块  
    chunk = 1024  
      
    #只读方式打开wav文件。wave只能播放wav文件，不能播放MP3
#     f = wave.open(r"night.wav","rb")  
    f = wave.open(r"night-30s.wav","rb")  
#     f = wave.open(r"night-all.wav","rb")  
      
    p = pyaudio.PyAudio()  
      
    #打开数据流  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)  
      
    #读取数据  
    data = f.readframes(chunk)  
      
    #播放  
    while data !="":  
        stream.write(data)  
        data = f.readframes(chunk)  
      
    #停止数据流  
    stream.stop_stream()  
    stream.close()  
      
    #关闭 PyAudio  
    p.terminate()  

if __name__ == '__main__':  
    start = time.time()
    print(start)
    play()
    end = time.time()
    print(end)
    print('takes: ' + str(end-start))


