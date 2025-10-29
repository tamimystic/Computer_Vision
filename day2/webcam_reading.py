import cv2
import os

#reading frame from webcam
webcam=cv2.VideoCapture(0) # here 0 means default webcam, but if i need to access my multiple camra just push camara port number

#set window size
webcam=set(3,640) #in cv2 3 means width
webcam=set(4,480) #in cv2 4 means height

while True:
    success,frame=webcam.read()
    cv2.imshow("Webcam frame", frame)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break