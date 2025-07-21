import time
import RPi.GPIO as GPIO
from picamera2 import Picamera2, Preview

button_pin = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Picamera2 객체 생성
picam2 = Picamera2()

# 프리뷰 설정
preview_config = picam2.create_preview_configuration(main={"format": "YUYV"})
picam2.configure(preview_config)
picam2.start_preview(Preview.QTGL)
picam2.start()

# 자동 노출/화이트밸런스 안정화 대기
print("카메라 설정 안정화 대기 중...")
time.sleep(2)

# 안정된 metadata 추출 (반복 시도)
exposure_time = None
analogue_gain = None

print("자동 설정값 추출 중...")

for i in range(10):  # 최대 10번 시도
    metadata = picam2.capture_metadata()
    if "ExposureTime" in metadata and "AnalogueGain" in metadata:
        exposure_time = metadata["ExposureTime"]
        analogue_gain = metadata["AnalogueGain"]
        print("자동 설정값 추출 성공!")
        break
    else:
        time.sleep(0.2)

# 실패 시 기본값 지정
if exposure_time is None:
    print("⚠️ ExposureTime 값이 없어 기본값 사용합니다.")
    exposure_time = 10000  # 10ms
if analogue_gain is None:
    print("⚠️ AnalogueGain 값이 없어 기본값 사용합니다.")
    analogue_gain = 1.0

print(f"노출 시간: {exposure_time}")
print(f"아날로그 게인: {analogue_gain}")

# 저장용 스틸 설정 (AWB는 자동에 맡김)
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
    time.sleep(1)
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
