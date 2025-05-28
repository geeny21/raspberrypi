'''
서보모터 제어
서보모터 제어핀 : GPIO21

서보모터 제어용 신호 주기 : 20ms
-> 주파수 : 50Hz
제어신호 1ms ~ 2ms
서보모터 제어용 신호의 듀티비 : 5% ~ 10%
0도 -> 90도 -> 180도로 위치 변경 후 종료

Duty Cycle:
5% -> 7.5% -> 10%

서보모터에 따라 동작 duty cycle 범위가 다를 수 있다.
2.5 ~ 12.5% 범위로 동작하는 서보모터도 있다.
'''

import RPi.GPIO as GPIO
import time

servo_pin = 21

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)

    pwm = GPIO.PWM(servo_pin, 50)  # 50Hz 주파수로 PWM 객체 생성
    pwm.start(0)  # PWM 신호를 0% 듀티 사이클로 시작

    print('Servo motor control start')
    
    # 서보모터를 0도 위치로 이동
    print('Moving to 0 degrees')
    pwm.ChangeDutyCycle(5)  # 듀티 사이클을 5%로 변경 (약 0도)
    time.sleep(1)  # 1초 동안 유지

    # 서보모터를 90도 위치로 이동
    print('Moving to 90 degrees')
    pwm.ChangeDutyCycle(7.5)  # 듀티 사이클을 7.5%로 변경 (약 90도)
    time.sleep(1)  # 1초 동안 유지

    # 서보모터를 180도 위치로 이동
    print('Moving to 180 degrees')
    pwm.ChangeDutyCycle(10)  # 듀티 사이클을 10%로 변경 (약 180도)
    time.sleep(1)

except KeyboardInterrupt:
    print("Key interrupt")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    pwm.stop()
    del pwm
    GPIO.cleanup()
print('Program end')
# print('Servo motor control end')