#-*- coding: UTF-8 -*-
'''
播放音频的例子
Created on 2017年10月14日

@author: Administrator
'''
import time
import vlc

# https://www.olivieraubert.net/vlc/python-ctypes/doc/
# vlcIns = vlc.Instance()
# oMediaPlayer = vlcIns.media_player_new()
# def playByVlc(sFilePath):
#     oMediaPlayer.set_media(vlcIns.media_new_path(sFilePath))
#     oMediaPlayer.play()
    
    
if __name__ == '__main__':  
    start = time.time()
    print(start)
#     playByVlc('E:/github/PythonStudy/PythonStudy/src/audioDemo/night-30s.wav')
    end = time.time()
    print(end)
    print('takes: ' + str(end-start))
    
        