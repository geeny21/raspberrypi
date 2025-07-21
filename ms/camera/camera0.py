'''
picamera를 이용한 사진 촬영
버튼 누르면 사진 촬영
버튼 : GPIO05, pull down
'''
import time
import RPi.GPIO as GPIO
from picamera2 import Picamera2

button_pin = 5

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 카메라 객체 생성
picam2 = Picamera2()
config = picam2.create_still_configuration(display="main")
picam2.configure(config)
picam2.start()

def capture_image():
    filename = time.strftime("/home/pi/work/raspberrypi/ms/camera/photo_%Y%m%d_%H%M%S.jpg")
    picam2.capture_file(filename)
    print(f"사진 저장 완료: {filename}")

try:
    print("버튼을 누르면 사진이 촬영됩니다.")
    while True:
        if GPIO.input(button_pin) == GPIO.HIGH:  # 버튼 누름 감지
            capture_image()
            time.sleep(0.5)  # 채터링 방지를 위한 대기
except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    picam2.close()
    GPIO.cleanup()
