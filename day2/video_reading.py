import cv2
import os

#Reading Videos frames(images)
vid_image=cv2.VideoCapture("resources/video.mp4")
while True:
    success,frame= vid_image.read()
    #print(frame.shape)
    cv2.imshow("Video Frame",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break