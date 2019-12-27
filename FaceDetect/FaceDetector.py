import numpy as np
import cv2

font=cv2.FONT_HERSHEY_SIMPLEX
def faceDetect():
    eye_detect=False
    face_cascade=cv2.CascadeClassifier('haarcascade_frontface.xml')
    eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
    info = ''

    '''얼굴 검출과 눈 검출을 위한 데이터를 읽어 CascadeClassifier 객체를 생성한다.
    CascadeClassifier 는 효과적인 객체 검출 방법이다.
    여기 있는 파일들은 미리 학습을 시켜 둔 파일이다.
    '''

    try:
        print('카메라 로딩 중...')
        cap=cv2.VideoCapture(0)

        '''
        1번째 카메라는 0, 2번째 카메라는 1....
        ()안에 비디오파일 이름을 작성하면 비디오 파일이 실행된다.
        '''

    except:
        print("카메라 없음")
        return

    while True:
        ret,frame=cap.read()
        if not ret:
            break

        if eye_detect:
            info='Eye Detection on'
        else:
            info='Eye Detection off'

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,5)

        '''
        grayscale이미지를 입력하여 얼굴을 검출한다.
        얼굴이 검출되면 위치를 리스트로 리턴한다.
        위치는 (x,y,w,h) 와 같은 튜플이다.
        x와 y는 검출된 얼굴의 좌상단, w,h는 가로 및 세로 크기이다.
        위 함수의 1.3은  ScaleFactor, 5는 minNeighbor 이다.
        '''

        cv2.putText(frame,info,(5,15),font,0.5,(255,0,255),1)

        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,'Detected Face',(x-5,y-5),font,0.5,(255,255,0),2)
            if eye_detect:
                roi_gray=gray[y:y+h,x:x+w]
                roi_color=frame[y:y+h,x:x+w]
                eyes=eye_cascade.detectMultiScale(roi_gray)

                '''
                사람 눈은 얼굴에 붙어 있다. 따라서 검출된 얼굴 안에서 눈을 찾으면 된다.
                눈이 검출되면, 그 위치를 리스트로 리턴한다.
                '''

                for(ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            cv2.imshow('frame',frame)
            k=cv2.waitKey(30)
            if k==ord('i'):
                eye_detect=not eye_detect
            if k==27:
                break

    cap.release()
    cv2.destroyAllWindows()

faceDetect()