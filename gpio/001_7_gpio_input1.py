'''
푸시버튼의 입력 상태를 화면에 출력
0.1초 단위로 상태를 확인
Ctrl+C 누르면 프로그램 종료
푸시버튼 : BCM gpio5
'''
import RPi.GPIO as GPIO
import time

# GPIO setup
BUTTON_GPIO = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # 내부 풀다운 저항 사용

print("Press the button connected to GPIO5 (Ctrl+C to exit)")

try:
    while True:
        button_state = GPIO.input(BUTTON_GPIO)
        # 버튼에 풀다운 저항이 연결되어 있으므로
        if button_state == GPIO.HIGH:
            print("Button Pressed")
        else:
            print("Button Released")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting program")
finally:
    GPIO.cleanup()