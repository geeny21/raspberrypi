'''
PWM
GPIO17에 PWM 신호 출력
0.1초 단위로 점점 밝아졌다가 점점 어두워지는 LED 제어
'''
import RPi.GPIO as GPIO
import time

led_pin = 17           # LED가 연결된 GPIO 핀 번호

#GPIO.setwarnings(False)  # GPIO 경고 메시지 비활성화

GPIO.setmode(GPIO.BCM) # 핀 번호 모드 설정 (BCM 방식)
GPIO.setup(led_pin, GPIO.OUT) # 핀을 출력으로 설정

pwm = GPIO.PWM(led_pin, 500)  # PWM 객체 생성, 500Hz 주파수
pwm.start(0)                  # 듀티 사이클 0%로 PWM 시작 (LED 꺼짐)

try:
    # LED 밝기 증가
    for duty in range(0, 101, 5):   # 0% ~ 100%까지 5%씩 증가
        pwm.ChangeDutyCycle(duty)   # 듀티 사이클 변경  
        print(f"Duty Cycle: {duty}%")
        time.sleep(0.1)
    
    # LED 밝기 감소
    for duty in range(100, -1, -5): # 100% ~ 0%까지 5%씩 감소
        pwm.ChangeDutyCycle(duty)
        print(f"Duty Cycle: {duty}%")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Key interrupt")
except :
    print("An error occurred or program interrupted.")
finally:
    pwm.stop()        # PWM 중지
    del pwm             # PWM 객체 삭제
    GPIO.cleanup()    # GPIO 리소스 정리
print('Program end')  # 프로그램 종료 메시지 출력
