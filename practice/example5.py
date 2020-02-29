#얼굴과 눈 검출하기

import cv2

cap = cv2.VideoCapture("http://192.168.0.24:7500/?action=stream")
face_pattern = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_pattern.detectMultiScale(gray, 1.5)
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        eye_gray = gray[y:y + h, x:x + h]
        eye_color = frame[y:y + h, x:x + h]
        eyes = eye_cascade.detectMultiScale(eye_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(eye_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 3)

    cv2.imshow('image', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()