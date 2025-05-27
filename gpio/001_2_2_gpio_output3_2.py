'''
3개의 led 제어
gpio17, 27, 22에 led 연결
1초 단위로 순차적으로 점멸
Ctrl+C 누르면 프로그램 종료
'''
import RPi.GPIO as GPIO
import time

led_pin = [17, 27, 22]

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

try :       # 개발자가 작성하고자 하는 목적 코드들
    while True :
        for pin in led_pin:
            GPIO.output(pin, True)
            print(f'Led {pin} on')

            time.sleep(1.0)

            GPIO.output(pin, False)
            print(f'Led {pin} off')
            time.sleep(1.0) 

except KeyboardInterrupt :  # Ctrl+C 누르면 KeyboardInterrupt 예외 발생  
    print("Key interrupt")
except :    # 오류로 인해 종려하는 경우
    pass    # 오류 처리 코드
finally :   # 종료하는  모든 경우(정상/오류로 인한 종료)에 실행되는 코드
    GPIO.cleanup()
print('Program end')