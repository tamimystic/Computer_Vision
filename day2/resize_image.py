import cv2

#Reading image
img=cv2.imread("resources\car.jpg")
print(img)
img_dekha=cv2.imshow("car image",img)
print(img.shape)
resize_image=cv2.resize(img,(500,400))
print(resize_image.shape)
resize_img_dekha=cv2.imshow("resize img", resize_image)
cv2.waitKey(0)