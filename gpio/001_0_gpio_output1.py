'''
gpio17에 led 연결
프로그램 시작하면 led on
Ctrl C 눌러 프로그램 종료
'''
import RPi.GPIO as GPIO

led_pin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

GPIO.output(led_pin, True)
print('Led on')

try:
    while True :
        pass
except KeyboardInterrupt :
    #pass
    print('keyboard interrupt')

GPIO.cleanup()
print('Program end')