'''
푸시버튼의 입력 상태를 화면에 출력
이벤트 기반 동작
0.1초 단위로 상태를 확인
Ctrl+C 누르면 프로그램 종료
푸시버튼 : BCM gpio5
        내부 pull-down 저항 사용
'''
import RPi.GPIO as GPIO
import time

num = 0


# button의 callback 함수
def button_callback(channel):
    global num
    num += 1
    if GPIO.input(channel) == GPIO.HIGH:
        print("Button Pressed")
    else:
        print("Button Released")
    print("Button Pressed count : ", num)

# GPIO setup
BUTTON_GPIO = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # 내부 풀다운 저항 사용

# Event 방식으로 Rising edge 감지
# bouncetime : 200ms 이내에 다시 이벤트 발생하지 않도록 설정
# rising edge를 검출하고자 GPIO.RASIONG으로 설정할 경우, Press Release 시에도 callback이 발생함
#GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING, callback=button_callback, bouncetime=200)

# falling edge를 검출하고자 GPIO.FALLING으로 설정할 경우, Press 시에 callback이 발생함
#GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, callback=button_callback, bouncetime=200)

# rasing/falling edge를 모두 검출하고자 GPIO.BOTH으로 설정할 경우, Press Release 시에도 callback이 발생함
GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, callback=button_callback, bouncetime=200)

print("Press the button connected to GPIO5 (Ctrl+C to exit)")

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting program")
finally:
    GPIO.cleanup()