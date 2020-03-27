import cv2 as cv
import numpy as np


#mask要大一圈
def fill_color_demo(image):
    copyimg = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    cv.floodFill(copyimg, mask, (400, 250), (0, 255, 255), (100, 100, 100), (50, 50, 50),  cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('fill_color_demo', copyimg)


#mask要大一圈
def fill_binary():
    image = np.zeros([400,400,3], np.uint8)
    image[100:300, 100:300, :] = 255
    mask = np.ones([402,402,1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow('fill_binary', image)




src = cv.imread('Highschool.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
#ROI region of interest
face = src[200:650, 300:600]

fill_color_demo(src)
cv.waitKey(0)


#销毁窗口
cv.destroyAllWindows()