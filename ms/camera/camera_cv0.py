'''
Opencv를 이용한 사진 촬영
버튼 누르면 사진 촬영
버튼 : GPIO05, pull down

'''
import cv2
import RPi.GPIO as GPIO
import time
from datetime import datetime

button_pin = 5  # 사진 촬영을 위한 버튼(GPIO05, physical pin은 29번 등)

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 카메라 장치 열기 (보통 0번 장치가 첫 번째 웹캠)
camera = cv2.VideoCapture(0)

def capture_image():
    ret, frame = camera.read()
    if ret:
        filename = datetime.now().strftime("/home/pi/work/raspberrypi/ms/camera/opencv_photo_%Y%m%d_%H%M%S.jpg")
        cv2.imwrite(filename, frame)
        print("사진 저장 완료:", filename)
    else:
        print("카메라로부터 이미지를 읽을 수 없습니다.")

try:
    print("버튼을 누르면 사진이 촬영됩니다.")
    while True:
        if GPIO.input(button_pin) == GPIO.HIGH:  # 버튼이 눌렸을 때
            print("버튼 감지, 사진 촬영 중...")
            capture_image()
            time.sleep(0.5)  # 채터링 방지
except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    camera.release()
    GPIO.cleanup()
