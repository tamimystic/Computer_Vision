import cv2
import numpy as np

img1=cv2.imread("resources\me.jpg")
img2=cv2.imread("resources\siberian-tiger.jpg")
print(img1.shape)
print("**********************************************")
print(img2.shape)

img_HOrizontal=np.hstack((img1,img1))
cv2.imshow("Horizontal Image",img_HOrizontal)
cv2.waitKey(0)

img_vertical=np.vstack((img1,img1))
cv2.imshow("Vertical Image",img_vertical)
cv2.waitKey(0)
