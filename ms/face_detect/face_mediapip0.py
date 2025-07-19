'''
mediapipe를 이용한 얼굴인식
인식한 얼굴에 사각형 표형
랜드마크 표시 - 눈, 코, 입, 귀에 빨간 원 표시

pip install mediapipe
pip install opencv-python
'''
import cv2
import mediapipe as mp

import time

# MediaPipe 세팅
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# 웹캠(또는 비디오) 열기
cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(
        model_selection=0,    # 0: 근거리, 1: 원거리 모델
        min_detection_confidence=0.5) as face_detection:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("카메라를 찾을 수 없습니다.")
            break

        # 영상 좌우반전 및 컬러 변환(BGR→RGB)
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # 얼굴 검출
        results = face_detection.process(image)

        # 다시 쓰기 가능하게끔 설정 및 컬러 복원
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 얼굴 위치 및 박스 그리기
        face_count = 0
        if results.detections:
            face_count = len(results.detections)
            # print(results.detections)
            # time.sleep(10)
            # print("*" *20)
            # 각 얼굴에 대해 박스와 라벨 그리기
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)
                            

        # 얼굴 개수 화면에 출력
        cv2.putText(
            image,
            f"Faces: {face_count}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # 화면에 결과 출력
        cv2.imshow('MediaPipe Face Detection', image)

        if cv2.waitKey(5) & 0xFF == 27: # ESC로 종료
            break

cap.release()
cv2.destroyAllWindows()
