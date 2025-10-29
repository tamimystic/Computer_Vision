import cv2
import numpy as np

img=np.zeros((400,400,3), np.uint8) #unit8 holo format
print(img)
cv2.imshow("without set color img", img)

img[:]=0,255,0
print(img)
cv2.imshow("set color img", img)
cv2.waitKey(0)
