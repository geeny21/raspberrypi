'''
눈을 감았는지 떳는지 확인하는 코드입니다.
얼굴을 인식하고 눈의 상태를 확인합니다.
눈을 감았으면 '눈을 감았습니다.'라고 출력합니다.
눈을 떳으면 '눈을 떴습니다.'라고 출력합니다.
얼굴을 인식하지 못하면 '얼굴을 인식하지 못했습니다.'라고 출력합니다.
눈을 감았는지 떳는지 확인하는 코드는 OpenCV와 mediapipe를 사용합니다.
OpenCV는 영상처리 라이브러리이고, mediapipe는 구글에서 개발한 머신러닝 라이브러리입니다.
이 코드는 웹캠을 통해 실시간으로 얼굴을 인식하고 눈의 상태를 확인합니다.    
'''
import cv2
import mediapipe as mp
import numpy as np

# EAR 계산 함수
# EAR(Eye Aspect Ratio)는 눈의 수평과 수직 길이 비율을 계산하여 눈의 상태를 판단하는 지표입니다.
# 눈의 수평 길이는 눈의 좌우 거리를, 수직 길이는 눈의 위아래 거리를 의미합니다.
# 눈이 감겨있을 때 EAR 값이 작아지고, 눈이 뜨여있을 때 EAR 값이 커집니다.
# 이 함수는 눈의 주요 랜드마크를 이용하여 EAR 값을 계산합니다.
# landmarks: mediapipe에서 추출한 얼굴 랜드마크 리스트
# indices: 왼쪽 눈과 오른쪽 눈의 주요 랜드마크 인덱스 리스트
# 반환값: 눈의 EAR 값
#
# 눈의 주요 랜드마크 인덱스는 mediapipe face_mesh에서 제공하는 인덱스를 사용합니다.
# 왼쪽 눈: [33, 160, 158, 133, 153, 144]
# 오른쪽 눈: [362, 385, 387, 263, 373, 380]
# 이 인덱스는 눈의 좌우, 위아래 위치를 나타내며, 이를 이용하여 눈의 수평과 수직 길이를 계산합니다.
# 수평 길이는 눈의 좌우 거리를, 수직 길이는 눈의 위아래 거리를 의미합니다.
# 눈의 좌우 거리는 왼쪽 눈의 왼쪽 끝과 오른쪽 눈의 오른쪽 끝 사이의 거리로 계산합니다.
# 눈의 위아래 거리는 눈의 위쪽 두 점과 아래쪽 두 점 사이의 평균 거리로 계산합니다.
# 이때, 좌표는 정규화된 값이므로 y좌표만 곱해주면 됩니다.
# EAR 값은 수직 길이를 수평 길이로 나눈 값으로,
# 눈이 감겨있을 때 EAR 값이 작아지고, 눈이 뜨여있을 때 EAR 값이 커집니다.
# 일반적으로 EAR 값이 0.20에서 0.23 사이일 때 눈이 감겨있다고 판단합니다.
# 이 값은 경험적으로 결정된 값으로, 상황에 따라 조정할 수 있습니다.
# 눈의 EAR 값을 계산하는 함수입니다.
# 이 함수는 눈의 주요 랜드마크를 이용하여 눈의 수평과 수직 길이를 계산하고,
# 이를 이용하여 EAR 값을 계산합니다.
# EAR 값은 눈의 상태를 판단하는 지표로 사용됩니다.
# 눈이 감겨있을 때 EAR 값이 작아지고, 눈이 뜨여있을 때 EAR 값이 커집니다.
# 이 함수는 mediapipe에서 추출한 얼굴 랜드마크 리스트와
# 왼쪽 눈과 오른쪽 눈의 주요 랜드마크 인덱스를 이용하여 EAR 값을 계산합니다.
# 반환값은 눈의 EAR 값입니다.
#
# mediapipe face_mesh에서 제공하는 왼쪽 눈과 오른쪽 눈의 주요 랜드마크 인덱스를 사용하여
# 눈의 좌우, 위아래 위치를 나타내며, 이를 이용하여 눈의 수평과 수직 길이를 계산합니다.
# 수평 길이는 눈의 좌우 거리를, 수직 길이는 눈의 위아래 거리를 의미합니다.
# 눈의 좌우 거리는 왼쪽 눈의 왼쪽 끝과 오른쪽 눈의 오른쪽 끝 사이의 거리로 계산합니다.
# 눈의 위아래 거리는 눈의 위쪽 두 점과 아래쪽 두 점 사이의 평균 거리로 계산합니다.
# 이때, 좌표는 정규화된 값이므로 y좌표만 곱해주면 됩니다.
# EAR 값은 수직 길이를 수평 길이로 나눈 값으로,
# 눈이 감겨있을 때 EAR 값이 작아지고, 눈이 뜨여있을 때 EAR 값이 커집니다.
# 일반적으로 EAR 값이 0.20에서 0.23 사이일 때 눈이 감겨있다고 판단합니다.
# 이 값은 경험적으로 결정된 값으로, 상황에 따라 조정할 수 있습니다.
# 눈의 EAR 값을 계산하는 함수입니다.
# 이 함수는 눈의 주요 랜드마크를 이용하여 눈의 수평과 수직 길이를 계산하고,
# 이를 이용하여 EAR 값을 계산합니다.
# EAR 값은 눈의 상태를 판단하는 지표로 사용됩니다.
# 눈이 감겨있을 때 EAR 값이 작아지고, 눈이 뜨여있을 때 EAR 값이 커집니다.
# 이 함수는 mediapipe에서 추출한 얼굴 랜드마크 리스트와
# 왼쪽 눈과 오른쪽 눈의 주요 랜드마크 인덱스를 이용하여 EAR 값을 계산합니다.
# 반환값은 눈의 EAR 값입니다.
def eye_aspect_ratio(landmarks, indices):
    left = np.array([landmarks[indices[0]].x, landmarks[indices[0]].y])
    right = np.array([landmarks[indices[3]].x, landmarks[indices[3]].y])
    top1 = np.array([landmarks[indices[1]].x, landmarks[indices[1]].y])
    top2 = np.array([landmarks[indices[2]].x, landmarks[indices[2]].y])
    bottom1 = np.array([landmarks[indices[5]].x, landmarks[indices[5]].y])
    bottom2 = np.array([landmarks[indices[4]].x, landmarks[indices[4]].y])
    # 거리는 정규화된 좌표(y만 곱해주면 됨)
    horizontal = np.linalg.norm(left - right)
    vertical = (np.linalg.norm(top1 - bottom1) + np.linalg.norm(top2 - bottom2)) / 2.0
    return vertical / horizontal

LEFT_EYE_IDX = [33, 160, 158, 133, 153, 144]  # mediapipe face_mesh 왼쪽 눈 주요 포인트
RIGHT_EYE_IDX = [362, 385, 387, 263, 373, 380] # 오른쪽 눈

mp_face_mesh = mp.solutions.face_mesh

cap = cv2.VideoCapture(0)
with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # 좌우반전, RGB 변환
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)
        h, w, _ = frame.shape
        if results.multi_face_landmarks:
            for landmarks in results.multi_face_landmarks:
                # 랜드마크 추출
                lms = landmarks.landmark
                leftEAR = eye_aspect_ratio(lms, LEFT_EYE_IDX)
                rightEAR = eye_aspect_ratio(lms, RIGHT_EYE_IDX)
                ear = (leftEAR + rightEAR) / 2.0

                # 눈 감음 기준값(EAR threshold) - 경험적으로 0.20~0.23
                if ear < 0.21:
                    state = "Closed"
                    color = (0, 0, 255)
                else:
                    state = "Open"
                    color = (0, 255, 0)
                cv2.putText(frame, f'Eyes: {state} ({ear:.2f})', (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        cv2.imshow("Eye Close Detection", frame)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC 종료
            break

cap.release()
cv2.destroyAllWindows()
