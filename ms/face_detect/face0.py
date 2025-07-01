'''
OpenCV를 이용한 얼굴인식 V1
카메라의 영상을 입력받기
그리고 얼굴을 인식하여 사각형으로 표시하는 프로그램입니다.

OpenCV 라이브러리를 설치해야 합니다.
설치 명령어: pip install opencv-python
프로그램 종료는 'q' 키를 누르면 됩니다.
프로그램 종료 시 'Program end' 메시지를 출력합니다.
'''
import cv2

def main():
    # 카메라 영상 입력
    # 0은 기본 카메라를 의미합니다. 다른 카메라를 사용하려면 1, 2 등으로 변경할 수 있습니다.
    cap = cv2.VideoCapture(0)

    # 얼굴 인식용 분류기 로드
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # cv2.data.haarcascades : OpenCV에서 제공하는 Haar Cascade 분류기 파일이 저장된 디렉토리입니다.
    # Haar Cascade 분류기는 객체 인식을 위한 머신 러닝 기반의 방법입니다.
    # 이 디렉토리에는 다양한 Haar Cascade 분류기 파일이 포함되어 있습니다
    # 예를 들어, 얼굴 인식, 눈 인식, 고양이 얼굴 인식 등을 위한 분류기 파일이 있습니다.
    # haarcascade_frontalface_default.xml : # 얼굴 인식을 위한 Haar Cascade 분류기 파일입니다.
    # 이 파일은 OpenCV에서 제공하는 기본 얼굴 인식 모델로, 얼굴을 인식하는 데 사용됩니다.
    
    while cap.isOpened():  # 카메라가 열려 있는지 확인
        # 카메라로부터 프레임 읽기
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        copied_frame = frame.copy()  # 프레임 복사 (원본 프레임을 유지하기 위해)
        # 얼굴 인식
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 프레임을 그레이스케일로 변환
        # 얼굴 인식은 일반적으로 그레이스케일 이미지에서 수행됩니다.
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)    # 얼굴 인식 수행
        # detectMultiScale() 함수는 이미지에서 객체(여기서는 얼굴)를 인식하는 함수입니다.
        # gray : 입력 이미지 (그레이스케일)
        # scaleFactor : 이미지 크기를 조정하는 비율입니다. 1.1은 이미지 크기를 10%씩 줄여가며 인식합니다.
        # minNeighbors : 인식된 객체가 최소 몇 개의 이웃 객체를 가져야 인식으로 간주할지를 결정합니다.
        # 이 값이 클수록 인식의 정확도가 높아지지만, 인식률이 낮아질 수 있습니다.
        # 반환값 faces는 인식된 얼굴의 좌표와 크기를 포함하는 리스트입니다.
        # 각 얼굴은 (x, y, w, h) 형태로 표현됩니다. 
        
        #print(faces)  # 인식된 얼굴 좌표 출력 (디버깅용)
        print('faces detected Number :', len(faces))    # 인식된 얼굴의 개수 출력
        
        if len(faces) :

            # 얼굴 영역에 사각형 그리기
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # 결과 영상 출력
            cv2.imshow('Face Detection', frame)

            # 'q' 키를 누르면 종료
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            # 얼굴이 인식되지 않은 경우, 원본 프레임을 출력
            cv2.imshow('Face Detection', copied_frame) 
    # 자원 해제
    cap.release()
    cv2.destroyAllWindows()


# 이 프로그램을 직접 실행할 때만 실행되는 코드
if __name__ == "__main__":
    main()
    print('Program end')  # 프로그램 종료 메시지 출력