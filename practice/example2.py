import cv2
import numpy as np

img1=cv2.imread('img1.jpg')  #이미지 불러들이기
img2=cv2.imread('img2.jpg')

def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('w','image',0,100,nothing)

while True:
    w=cv2.getTrackbarPos('w','image')  #w는 0~100까지의 값, 트랙바에서 끌어옴
    dst=cv2.addWeighted(img1,float(100-w)*0.01,img2,float(w)*0.01,0)
    cv2.imshow('dst',dst) #결과값 이미지 출력

    if cv2.waitKey(1) & 0xFF == 27: #esc 클릭했을 경우에 창 종료
        break;

cv2.destroyAllWindows()