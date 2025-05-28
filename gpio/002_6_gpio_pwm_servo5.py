'''
서보모터 제어
서보모터 제어핀 : GPIO21

서보모터 제어용 신호 주기 : 20ms
-> 주파수 : 50Hz
제어신호 1ms ~ 2ms
서보모터 제어용 신호의 듀티비 : 5% ~ 10%  (2.5~12.5%)

사용자로부터 Duty cycle을 입력받아 서보모터의 위치 지정
함수 servo(angle) 정의
'''
import RPi.GPIO as GPIO
import time

# def map(value, from_min, from_max, to_min, to_max):
#     """주어진 범위에서 값을 다른 범위로 매핑하는 함수"""
#     return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min      

def servo(duty_cycle):
    if duty_cycle < 0 or duty_cycle > 100:
        print("Angle must be between 0 and 180 degrees.")
        return   # 잘못된 각도 입력 처리

    #duty_cycle = (angle / 18) + 2.5  # 각도를 듀티 사이클로 변환
    #duty_cycle = map(angle, 0, 180, 5, 10)  # 각도를 듀티 사이클로 변환 (5% ~ 10%)
    #print(f'Setting servo to {angle} degrees (Duty Cycle: {duty_cycle}%)')
    pwm.ChangeDutyCycle(duty_cycle)  # 듀티 사이클 변경
    #time.sleep(1)  # 1초 동안 유지

servo_pin = 21

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)

    pwm = GPIO.PWM(servo_pin, 50)  # 50Hz 주파수로 PWM 객체 생성
    pwm.start(0)  # PWM 신호를 0% 듀티 사이클로 시작

    print('Servo motor control start')
    
    while True :
        angle = input("Enter duty cycle (0-100 %) or 'q' to quit: ")
        if angle.lower() == 'q':
            break
        
        angle = float(angle)  # 입력값을 실수로 변환
        servo(angle)  # 서보모터 위치 지정
        time.sleep(1)  # 1초 동안 유지
        
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