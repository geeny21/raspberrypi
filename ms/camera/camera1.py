'''
picamera를 이용한 사진 촬영
버튼 누르면 사진 촬영
버튼 : GPIO05, pull down

촬영  결과가 어둡다.
'''

import time
import RPi.GPIO as GPIO
from picamera2 import Picamera2, Preview

button_pin = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

picam2 = Picamera2()
# 프리뷰 & 저장 설정을 나눔
preview_config = picam2.create_preview_configuration(main={"format": "YUYV"})
still_config = picam2.create_still_configuration(main={"format": "RGB888"})   # [수정] 저장용 설정

picam2.configure(preview_config)
picam2.start_preview(Preview.QTGL)
picam2.start()

def capture_image():
    # 저장 전 스틸 모드로 전환
    filename = time.strftime("/home/pi/work/raspberrypi/ms/camera/photo_%Y%m%d_%H%M%S.jpg")
    time.sleep(2)  # 카메라 안정화 대기
    picam2.switch_mode_and_capture_file(still_config, filename)    

    print("사진 저장 완료!")

try:
    print("버튼을 누르면 사진이 촬영됩니다.")
    while True:
        if GPIO.input(button_pin) == GPIO.HIGH:
            print("버튼이 눌렸습니다. 사진 촬영 중...")
            capture_image()
            time.sleep(0.5)
except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    picam2.close()
    GPIO.cleanup()
