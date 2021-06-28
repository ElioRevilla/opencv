# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 17:56:00 2021

@author: elio_
"""

import os
import cv2
import numpy as np

import time
import datetime
#sys.path.append("..")

VIDEO_NAME = 'video.mp4'
video = cv2.VideoCapture(VIDEO_NAME)
currentFrame = 1


while(video.isOpened()):
    ret, frame = video.read()
    if ret == True: 
        name = './reporte/frame' + str(currentFrame) + '.jpg'                      
        status = cv2.imwrite(name,frame)
        currentFrame += 1
    else:
        continue
    
    print(currentFrame)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()