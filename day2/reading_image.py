import cv2
import os

#Reading image
img=cv2.imread("resources\me.jpg")
#print(img)
#print(type(img))
#print(img.shape) height,width,channels

cv2.imshow("My Image",img)
cv2.waitKey(0)

#Reading Videos frames(images)
'''vid_image=cv2.VideoCapture("resources\video.mp4")
while True:
    success,frame= vid_image.read()
    print(frame.shape)
print(vid_image) '''