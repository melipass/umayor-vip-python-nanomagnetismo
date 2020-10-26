# -*- coding: utf-8 -*-
import cv2
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc

width = 1920
height = 1080
FPS = 24
seconds = 10

radius = 150
paint_y = int(height/2)

fourcc = VideoWriter_fourcc(*'MP42')
video = VideoWriter('./noise.avi', fourcc, float(FPS), (width, height))
font = cv2.FONT_HERSHEY_DUPLEX

frame = np.zeros([height, width, 3],
                     dtype = np.uint8)

#Variables para modificar la altura a lo largo del video
amplitud = 10
valorSin = (np.pi / 2)

for paint_x in range(0, width, 10):
    #Cambiar color de fondo gradualmente
    for pixel in frame:
        pixel += 1
    
    #Borrar la cola de la figura
    cv2.rectangle(frame, (paint_x-10, paint_y), (paint_x+200, paint_y+200),
                  (frame.item(0),frame.item(0),frame.item(0)), -1)
    
    #Cambiar la altura
    paint_y += int(amplitud*np.sin(valorSin))
    valorSin += 0.1
    #Pintar la figura
    cv2.rectangle(frame, (paint_x, paint_y), (paint_x+200, paint_y+200),
                  (255,192,203), -1)
    
    #Texto
    cv2.putText(frame, "Cuadrado en movimiento sinusoidal", (75,150), font, 3,
                (255,255,255), 2, cv2.LINE_AA)
    
    
    video.write(frame)
    
    
video.release()

