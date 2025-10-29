import cv2

img=cv2.imread("resources\me.jpg")
print(img)

img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_gray) # from 3 channel to single channel

original_img_dekha=cv2.imshow("my original pic",img)
gray_img_dekha=cv2.imshow("gray scale img", img_gray)
cv2.waitKey(0)

