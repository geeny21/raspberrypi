'''
gpio17에 led 연결
2초 단위로 점멸
Ctrl+C 누르면 프로그램 종료
'''
import RPi.GPIO as GPIO
import time

led_pin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

try :
    while True :
        GPIO.output(led_pin, True)
        print('Led on')

        time.sleep(1.0)

        GPIO.output(led_pin, False)
        print('Led off')
        time.sleep(1.0)

except KeyboardInterrupt :
    print("Key interrupt")
GPIO.cleanup()
print('Program end')