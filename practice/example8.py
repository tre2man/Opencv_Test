#컨투어 예제

import cv2 as cv
import numpy as np


img_color = cv.imread('hand.png')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)


for cnt in contours:
    cv.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)  # blue

cv.imshow("result", img_color)

cv.waitKey(0)


for cnt in contours:

    hull = cv.convexHull(cnt)
    cv.drawContours(img_color, [hull], 0, (255, 0, 255), 5)


cv.imshow("result", img_color)

cv.waitKey(0)


for cnt in contours:
    hull = cv.convexHull(cnt, returnPoints = False)
    defects = cv.convexityDefects(cnt, hull)

    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])

        print(d)


        if d > 500:
            cv.line(img_color, start, end, [0, 255, 0], 5)
            cv.circle(img_color, far, 5, [0,0,255], -1)

        cv.imshow("result", img_color)
        cv.waitKey(0)