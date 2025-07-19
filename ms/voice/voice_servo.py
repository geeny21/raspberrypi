'''
마이크를 이용해 각도를 지시한다.
0~180의 값이면 서보모터가 해당 각도로 회전한다.
'종료'라고 이야기하면 프로그램을 종료한다.

문제점 : 180도 와 같이 숫자 이외의 다른 말이 들어오면 에러가 발생한다.
해결 : word2number 라이브러리를 이용해 숫자 이외의 말이 들어오면 예외처리한다.      
'''
import RPi.GPIO as GPIO
import time
import speech_recognition as sr
from word2number import w2n

# def map(value, from_min, from_max, to_min, to_max):
#     """주어진 범위에서 값을 다른 범위로 매핑하는 함수"""
#     return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min      

def servo(angle):
    if angle < 0 or angle > 180:
        print("Angle must be between 0 and 180 degrees.")
        return   # 잘못된 각도 입력 처리

    duty_cycle = (angle / 18) + 2.5  # 각도를 듀티 사이클로 변환
    #duty_cycle = map(angle, 0, 180, 5, 10)  # 각도를 듀티 사이클로 변환 (5% ~ 10%)
    print(f'Setting servo to {angle} degrees (Duty Cycle: {duty_cycle}%)')
    pwm.ChangeDutyCycle(duty_cycle)  # 듀티 사이클 변경
    #time.sleep(1)  # 1초 동안 유지

servo_pin = 21

recognizer = sr.Recognizer()
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)  # 50Hz 주파수로 PWM 객체 생성
pwm.start(0)  # PWM 신호를 0% 듀티 사이클로 시작

with sr.Microphone() as source:
    while True:
        print("숫자를 말하세요. (종료하려면 '종료'라고 말하세요)")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='ko-KR')
            print("인식된 음성:", text)
            if text in ["종료", "끝", "그만"]:
                print("프로그램을 종료합니다.")   
                break
            number = w2n.word_to_num(text)
            print("인식한 숫자값:", number)
            if number < 0 or number > 180:
                print("각도는 0에서 180 사이여야 합니다.")
                continue  # 잘못된 각도 입력 처리
            servo(number)  # 서보모터 위치 지정
            time.sleep(1)  # 1초 동안 유지  

        except Exception as e:
            print("에러:", e)
        except KeyboardInterrupt:
            print("프로그램을 종료합니다.")
            break   

            
pwm.stop()
del pwm
GPIO.cleanup()  # GPIO 설정 초기화  
print("GPIO cleanup completed.") 

