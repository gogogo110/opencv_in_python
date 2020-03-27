import cv2 as cv
import numpy as np


def extract_object_demo():
    capture = cv.VideoCapture('video.mp4')   #没有视频文件
    while True:
        ret, frame = capture.read()
        if ret == False:
            break
        #利用hsv色域图来对某种颜色进行挖掘
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        mask = cv.inRange(hsv, np.array([35,43,36]),np.array([77,255,255]))
        #dst=cv.bitwise_and(frame,frame,mask=mask)  提取出只有绿色圆盘的部分
        cv.imshow('video', frame)
        cv.imshow('mask',mask)
        c = cv.waitKey(40)
        if c == 27:
            break


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    print(hsv)
    cv.imshow('hsv', hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow('yuv', yuv)


'''
通道的和并与分离
b,g,r = cv.split(image)
image_new = cv.merge([b,g,r])
'''


src = cv.imread('Highschool.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)

extract_object_demo()
cv.waitKey(0)


#销毁窗口
cv.destroyAllWindows()