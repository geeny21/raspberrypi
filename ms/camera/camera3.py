'''
picamera를 이용한 사진 촬영
버튼 누르면 사진 촬영
버튼 : GPIO05, pull down

노출시간과 게인을 수동으로 반영

촬영  결과가 어둡다.
'''
import time
import RPi.GPIO as GPIO
from picamera2 import Picamera2, Preview

button_pin = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(main={"format": "YUYV"})
picam2.configure(preview_config)
picam2.start_preview(Preview.QTGL)
picam2.start()

# 노출·게인 값 조절 (환경에 따라 수정!)
exposure_time = 50000    # 1/20초 (50,000us)
analogue_gain = 2.0      # 게인 x2

print(f"노출 시간: {exposure_time}")
print(f"아날로그 게인: {analogue_gain}")

still_config = picam2.create_still_configuration(
    display="main",
    controls={
        "ExposureTime": exposure_time,
        "AnalogueGain": analogue_gain
    }
)

def capture_image():
    filename = time.strftime("/home/pi/work/raspberrypi/ms/camera/photo_%Y%m%d_%H%M%S.jpg")
    print("사진 촬영 준비 중... (카메라 안정화 대기)")
    time.sleep(1)  # preview 상태 안정화
    picam2.switch_mode_and_capture_file(still_config, filename)
    time.sleep(1)  # preview 상태 안정화
    picam2.switch_mode_and_capture_file(still_config, filename)
    print("사진 저장 완료! →", filename)

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
