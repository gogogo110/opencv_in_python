import cv2 as cv
import numpy as np
import time

def access_pixel(image):
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]
    print(image.shape,height, width, channel)
    for i in range(height):
        for j in range(width):
            for k in range(channel):
                image[i][j][k] = 255 - image[i][j][k]
    cv.imshow('new pic', image)

def access_pixel_c(image):
    dst = cv.bitwise_not(image)
    cv.imshow('new pic', dst)

def create_image():
    img=np.zeros([400,400,3], dtype=np.uint8)
    #数字图像逐像素进行操作
    cv.imshow('new pic', img)


src = cv.imread('Highschool.jpg')   #RGB
cv.namedWindow('new pic', cv.WINDOW_AUTOSIZE)
t1 = time.time()
access_pixel(src)
t2 = time.time()
print(t2-t1)
t1 = time.time()
access_pixel_c(src)
t2 = time.time()
print(t2-t1)

cv.waitKey(0)
cv.destroyAllWindows()


