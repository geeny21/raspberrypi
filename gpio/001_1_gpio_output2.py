'''
gpio17에 led 연결
프로그램 시작하면 led on
2초 뒤 프로그램 종료
'''
import RPi.GPIO as GPIO
import time

led_pin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

GPIO.output(led_pin, True)
print('Led on')

time.sleep(2.0)

GPIO.output(led_pin, False)
print('Led off')

GPIO.cleanup()
print('Program end')