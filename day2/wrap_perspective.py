import cv2
import numpy as np

width,height=250,350
img=cv2.imread("resources\card.jpg")

pts1=np.float32([[335,180],[496,226],[270,405],[430,453]]) #original image crop area ->top left->top right->bottom left->bottom right
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]]) #this is the area where we adjust our cropped image ->top left->top right->bottom left->bottom right

matrix=cv2.getPerspectiveTransform(pts1,pts2) #create transformation matrix (3*3), which decide that where and how to plot cropped image in new area(pts2)
single_card=cv2.warpPerspective(img,matrix,(width,height)) #apply perspective transformation to get the cropped image

cv2.imshow("Image",img)
cv2.imshow("Single card",single_card)
cv2.waitKey(0)