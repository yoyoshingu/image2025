# 얼굴인식 프로젝트
# opencv Harr filter를 연속적용하는 방식
# 2025.10.1
# 필터 다운로드 사이트
# https://github.com/opencv/opencv/tree/master/data/haarcascades

import cv2

# 얼굴 검출
face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_default.xml')

# 눈 검출
eye_cascade = cv2.CascadeClassifier('./recdata/haarcascade_eye.xml')


img = cv2.imread('img/image.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray)

# [[146  96 120 120]  [x, y, w, h]  => cv.rectangle((x, y), (x+w, y+h))
#  [398  97 106 106]]  [x, y, w, h]
print(faces)

# children.jpg
# cv2.rectangle(img, (146, 96), (120+146,120+96), (255, 0, 0), 5)
# cv2.rectangle(img, (398, 97), (106+398,106+97), (0, 255, 0), 5)

# boy_face.jpg
# cv2.rectangle(img, (146, 190), (146+306,190+306), (0, 255, 0), 5)

# image.png
# cv2.rectangle(img, (276, 68), (276+88,68+88), (0, 255, 0), 5)  # 이렇게하면 안됨

# 네모를 일반적으로 표시함
for face in faces:
    fx, fy, fw, fh = face
    cv2.rectangle(img, (fx, fy), (fx+fw, fy+fh), (0, 255, 0), 2)
    # 눈 검출 시작
    eyes = eye_cascade.detectMultiScale(gray[fy:fy+fh, fx:fx+fw])
    for eye in eyes:
        ex, ey, ew, eh = eye
        cv2.rectangle(img, (fx+ex, fy+ey), (fx+ex+ew, fy+ey+eh), (0, 0, 255), 2)



cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

