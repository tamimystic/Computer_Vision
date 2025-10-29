import cv2

#Reading image
img=cv2.imread("resources\me.jpg")
print(img)
print(img.shape)
cv2.imshow("My Image",img)

print("*****************croping image****************************")
crope_img=img[550:650,100:650]
print(crope_img.shape)
cv2.imshow("crope image",crope_img)
cv2.waitKey(0)