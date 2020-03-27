import cv2 as cv
import numpy as np


#加减乘除的操作要求图像大小相等
def add_demo(im1,im2):
    dst = cv.add(im1,im2)
    cv.imshow('add_demo',dst)


def subtract_demo(im1,im2):
    dst = cv.subtract(im1,im2)
    cv.imshow('subtract_demo',dst)


def divide_demo(im1, im2):
    dst = cv.divide(im1, im2)
    cv.imshow('divide_demo', dst)


def multiply_demo(im1, im2):
    dst = cv.multiply(im1, im2)
    cv.imshow('multiply_demo', dst)


#与或非逻辑运算
def logic_demo(im1,im2):
    dst = cv.bitwise_and(im1,im2)


#调整对比度和亮度
def contrast_brightness_demo(image,c,b):
    h, w, ch = image.shape
    blank = np.zeros([h,w,ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow('con-bri-demo', dst)


#还有cv.mean（），cv.meanStdDev()求均值和方差
src1 = cv.imread('Highschool.jpg')
#scr2=...
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src1)


cv.waitKey(0)


#销毁窗口
cv.destroyAllWindows()