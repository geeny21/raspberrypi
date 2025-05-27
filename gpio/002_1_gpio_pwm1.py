'''
PWM
GPIO17에 PWM 신호 출력
5초 단위로 듀티 사이클을 25%, 50%, 100%로 변경
'''
import RPi.GPIO as GPIO
import time

led_pin = 17

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, GPIO.LOW)  # LED를 켜기 위해 GPIO 핀을 LOW로 설정

    
    pwm = GPIO.PWM(led_pin, 100)  # 100Hz 주파수로 PWM 객체 생성
    pwm.start(0)  # PWM 신호를 0% 듀티 사이클로 시작

    print('Duty cycle : 25%')
    pwm.ChangeDutyCycle(25)  # 듀티 사이클을 25%로 변경
    time.sleep(5)  # 5초 동안 유지

    print('Duty cycle : 50%')
    pwm.ChangeDutyCycle(50)  # 듀티 사이클을 50%로 변경
    time.sleep(5)  # 5초 동안 유지

    print('Duty cycle : 100%')
    pwm.ChangeDutyCycle(100)  # 듀티 사이클을 100%로 변경
    time.sleep(5)  # 5초 동안 유지

    pwm.stop()  # PWM 신호 중지

except KeyboardInterrupt:
    print("Key interrupt")
except :
    pass
finally:
    pwm.stop()  # PWM 신호 중지
    del pwm             # PWM 객체 삭제 (객체삭제하지 않으면 프로그램 종료시 에러 발생)
    GPIO.cleanup()  # GPIO 핀 정리
print('Program end')
