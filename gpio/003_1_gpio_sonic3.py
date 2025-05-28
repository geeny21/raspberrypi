'''
초음파 센서

Trig : GPIO23
Echo : GPIO24 (3.3V : Logic Level Shifter 필요)

장애물과의 거리가 20cm 이하이면 LED 점등하고
메시지 출력  
단, 메시지는 상태변화시 한번만씩만 출력

LED : GPIO17
'''
import RPi.GPIO as GPIO
import time

# GPIO 핀 설정
TRIG_PIN = 23
ECHO_PIN = 24
LED_PIN = 17

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

GPIO.setup(LED_PIN, GPIO.OUT)

def get_distance():
    # 초음파 신호 전송
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)  # 10us 동안 HIGH 상태 유지
    GPIO.output(TRIG_PIN, False)

    # Echo 핀에서 신호 수신 대기
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # 시간 차이 계산
    pulse_duration = pulse_end - pulse_start

    # 거리 계산 (cm 단위)
    distance = pulse_duration * 34300 / 2   # Speed of sound is 34300 cm/s
    distance = round(distance, 2)  # 소수점 둘째 자리까지 반올림

    return distance

# LED 상태
led_state = False
print("LED OFF")

try:
    print("초음파 센서 작동 시작")
    while True:
        distance = get_distance()
        if distance <= 20:
            if not led_state:
                GPIO.output(LED_PIN, True)
                print("LED ON")
                led_state = True
        else:
            if led_state:
                led_state = False   
                GPIO.output(LED_PIN, False)
                print("LED OFF")

        # 거리 출력
        print(f"거리: {distance} cm")
        time.sleep(0.5)  # 0.5초 대기
except KeyboardInterrupt:   
    print("keyboard interrupt")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    GPIO.cleanup()
    print("GPIO 핀 정리 완료")
print("프로그램 종료")
# print("초음파 센서 작동 종료")