'''
타임랩스
opencv를 이용한 타임랩스 촬영
Preview 삭제 버전

1초 단위
'''
import cv2
import time
from datetime import datetime

# 카메라 장치 열기 (cv2.VideoCapture(0)은 첫 번째 카메라)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

save_dir = "/home/pi/work/raspberrypi/ms/camera/"  # 저장 경로 알맞게 설정

print("1초마다 자동으로 사진이 저장됩니다. 종료하려면 Ctrl+C 또는 q를 누르세요.")

try:
    while True:
        ret, frame = camera.read()
        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        filename = datetime.now().strftime(save_dir + "auto_photo_%Y%m%d_%H%M%S.jpg")
        cv2.imwrite(filename, frame)
        print(f"사진 저장 완료: {filename}")

        # 1초 대기
        time.sleep(0.5)

        # (옵션) 실시간 프리뷰
        #cv2.imshow("Auto Capture Preview", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("프로그램 수동 종료(Ctrl+C)")

finally:
    camera.release()
    cv2.destroyAllWindows()
