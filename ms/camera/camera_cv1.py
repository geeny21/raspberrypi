'''
Opencv를 이용한 사진 촬영
버튼 누르면 사진 촬영
버튼 : GPIO05, pull down

Preview 추가
'''
import cv2
import RPi.GPIO as GPIO
import time
from datetime import datetime

button_pin = 5  # GPIO 5번 핀 사용

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

camera = cv2.VideoCapture(0)  # 첫 번째 카메라 장치 사용

cv2.namedWindow("Camera Preview", cv2.WINDOW_NORMAL)

print("카메라 프리뷰 화면이 표시됩니다. 버튼을 누르면 사진이 촬영됩니다.")

try:
    while True:
        ret, frame = camera.read()
        if not ret:
            print("카메라를 찾을 수 없습니다.")
            break
        # 프리뷰 윈도우에 현재 프레임 표시
        cv2.imshow("Camera Preview", frame)

        # 버튼이 눌리면 이미지 저장
        if GPIO.input(button_pin) == GPIO.HIGH:
            filename = datetime.now().strftime("/home/pi/work/raspberrypi/ms/camera/opencv_photo_%Y%m%d_%H%M%S.jpg")
            cv2.imwrite(filename, frame)
            print(f"사진 저장 완료: {filename}")
            time.sleep(0.5)  # 채터링 방지(중복 촬영 방지)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("프로그램 종료")

finally:
    camera.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
