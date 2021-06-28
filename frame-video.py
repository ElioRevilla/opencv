# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:04:20 2021

@author: elio_
"""


import cv2
import os

from os.path import isfile, join

def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

    #ordenar las imagenes
    files.sort(key = lambda x: int(x[5:-4]))

    for i in range(len(files)):
        filename=pathIn + files[i]        
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)        
        frame_array.append(img)

    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(frame_array)):        
        out.write(frame_array[i])
    out.release()

def main():
    pathIn= './reporte/' # carpeta de imagenes
    pathOut = 'new-video.avi'
    fps = 25.0
    convert_frames_to_video(pathIn, pathOut, fps)

if __name__=="__main__":
    main()

