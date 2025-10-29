import cv2
import numpy as np

#create black image
img=np.zeros((400,400,3), np.uint8) #unit8 holo format
print(img)
cv2.imshow("without set color img", img)


#set green color to black image
img[:]=0,255,0 #bgr
print(img)
cv2.imshow("set color img", img)


#create lines
cv2.line(img,(0,200),(400,200),(0,0,255),3) #horizontal line, 3 means line thickness
cv2.line(img,(200,0),(200,400),(0,0,255),3) #vertical line
cv2.imshow("line img", img)


#creating rectangle
cv2.rectangle(img,(50,50),(150,150),(0,0,255),2) #first co-ordinate
cv2.rectangle(img,(250,50),(350,150),(0,0,255),cv2.FILLED) #second cordinate
cv2.imshow("rectangle img", img)


#creating circle
cv2.circle(img,(100,300),50,(0,0,255),2)
cv2.imshow("circle img", img)


#putting text on image
cv2.putText(img,"Tamim Hossain",(210,300),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,0),2)
cv2.imshow("text img", img)
cv2.waitKey(0)
