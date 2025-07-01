'''
OpenCV를 이용해서 영상을 받아보는 코드
'''

import cv2

def main() :
    # 카메라 영상 입력
    # 0은 기본 카메라를 의미합니다. 다른 카메라를 사용하려면 1, 2 등으로 변경할 수 있습니다.
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 프레임 너비 설정
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 프레임 높

    while cap.isOpened():   # 카메라가 열려 있는지 확인
        # 카메라로부터 프레임 읽기
        ret, frame = cap.read() # 프레임 읽기
        if not ret:
            break

        # 결과 영상 출력
        cv2.imshow('Camera Test', frame)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 자원 해제
    cap.release()
    cv2.destroyAllWindows()

# 이 프로그램을 직접 실행할 때만 실행되는 코드
if __name__ == "__main__":
    main()
    print('Program end')  # 프로그램 종료 메시지 출력