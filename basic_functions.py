import cv2
import numpy as np

img = cv2.imread("opencv_image.png")
# Check Image shape
print("image shape", img.shape)

# resize image (300 width and 200 height) - stretching does not improve quality
resizeImg = cv2.resize(img, (300,200))

# Crop Image - 180 to 248 height and width all
cropImg = img[180:248,:]

# convert color
GrayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image
BlurImg = cv2.GaussianBlur(img, (7,7), 2)

# Detect Edges
CannyImg = cv2.Canny(img, 100,200)

noiseImg = cv2.imread("dilation_example.jpg")

# Image Erosion -  mostly to remove noise
ErodeImg = cv2.erode(noiseImg, (7,7), iterations=5)

# Image dilation - Increases the object area
DilImg = cv2.dilate(ErodeImg, (5,5), iterations=3)


# save the images

cv2.imwrite("OutputImages/ResizeImage.png", resizeImg)
cv2.imwrite("OutputImages/CropImg.png", cropImg)
cv2.imwrite("OutputImages/GrayImage.png", GrayImg)
cv2.imwrite("OutputImages/GrayImage.png", GrayImg)
cv2.imwrite("OutputImages/BlurImage.png", BlurImg)
cv2.imwrite("OutputImages/CannyImage.png", CannyImg)
cv2.imwrite("OutputImages/ErodedImage.png", ErodeImg)
cv2.imwrite("OutputImages/DilatedImage.png", DilImg)

# display the images
cv2.imshow("OriginalImage", img)
cv2.imshow("ResizeImage", resizeImg)
cv2.imshow("CropImg", cropImg)
cv2.imshow("Gray Image", GrayImg)
cv2.imshow("Blur Image", BlurImg)
cv2.imshow("Canny Image", CannyImg)
cv2.imshow("Noise Image", noiseImg)
cv2.imshow("Erode Image", ErodeImg)
cv2.imshow("Dilate Image", DilImg)
cv2.waitKey(0)