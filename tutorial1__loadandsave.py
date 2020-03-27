import cv2 as cv


def video_demo():
    #将0换成文件路径也可以读取视频
    capture = cv.VideoCapture(0)
    while True:
        _, frame = capture.read()
        cv.imshow('video', frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_image_info(image):
    print(type(image))   #np.array
    print(image.shape)   #(533,799,3)
    print(image.size)    #12277601
    print(image.dtype)   #uint8
    #获取像素数据  np.array(image)


src = cv.imread('Highschool.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
video_demo()
cv.waitKey(0)


#销毁窗口
cv.destroyAllWindows()