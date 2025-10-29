import cv2

#Read original image
img=cv2.imread("resources\me.jpg")
print(img)
print(img.shape)
original_img_dekha=cv2.imshow("my original pic",img)


print("*********************gray scale image***********************")
#Convert original img to gray scale image
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_gray) # from 3 channel to single channel
print(img_gray.shape)
gray_img_dekha=cv2.imshow("gray scale img", img_gray)


print("*********************blur image***********************")
#Convert to blur image
img_blur=cv2.GaussianBlur(img_gray,(7,7),0) #kernel/filter size and 0 means density, tar mane kototuku blur hobe
print(img_blur)
print(img_blur.shape)
blur_img_dekha=cv2.imshow("blur image", img_blur)
#we convert to gray scale beacause reduce our complexity,beacause to convert blur we just want to know the edges


print("*********************edge cascade(canny) image***********************")
#Convert to edge cascade image 
img_canny=cv2.Canny(img_blur,100,100) #100,100 mane threshold value, that means jodi kono pixel er value 100 er besi hoy tahole seta edge hisebe consider kora hobe
print(img_canny)
print(img_canny.shape)
canny_img_dekha=cv2.imshow("canny image", img_canny)
cv2.waitKey(0)
