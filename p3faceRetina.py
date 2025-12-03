# 2025.12.3 이미지처리 소규모프로젝트
# 종강임
# 환경설정
# conda create -n imgretina python==3.9
# conda activate imgretina
# conda install conda-forge::retina-face
# pip install opencv-python

import cv2
from retinaface import RetinaFace


img_path = "./img/image.png"

faces = RetinaFace.detect_faces(img_path)
print(faces)


img = cv2.imread(img_path)
for key, face in faces.items():
    facial_area = face['facial_area']
    cv2.rectangle(img, (facial_area[0], facial_area[1]),
                  (facial_area[2], facial_area[3]), (255, 0,0), 2)
    cv2.putText(img, f"{face['score']:.3f}",
                (facial_area[0], facial_area[1]), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0))

#  참고 개발과정
# face1 = faces['face_1']
# print(face1)
# facial_area = face1['facial_area']
# print(facial_area)
# # children
# # 1st: 400, 95, 490, 208
# # 2nd: 155, 93, 251, 212




cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
