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

try :
    while True :
        for pin in led_pin:
            GPIO.output(pin, True)
            print(f'Led {pin} on')

            time.sleep(1.0)

            GPIO.output(pin, False)
            print(f'Led {pin} off')
            time.sleep(1.0) 

except KeyboardInterrupt :
    print("Key interrupt")
GPIO.cleanup()
print('Program end')