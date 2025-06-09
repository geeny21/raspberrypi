'''
GPIO 5 : 푸시버튼, 내부 풀업
GPIO 6 : 푸시버튼, 내부 풀다운
GPIO 17 : LED1
GPIO 27 : LED2
'''
import RPi.GPIO as GPIO
import time

def button1_callback(channel):
    print("Button 1 pressed")
    GPIO.output(led1_pin, GPIO.HIGH)
    GPIO.output(led2_pin, GPIO.LOW)


def button2_callback(channel):
    print("Button 2 pressed")
    GPIO.output(led2_pin, GPIO.HIGH)
    GPIO.output(led1_pin, GPIO.LOW)


BUTTON1_GPIO = 5
BUTTON2_GPIO = 6
led1_pin = 17
led2_pin = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(led1_pin, GPIO.OUT)
GPIO.setup(led2_pin, GPIO.OUT)
GPIO.setup(BUTTON1_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(BUTTON1_GPIO, GPIO.RISING, callback=button1_callback, bouncetime=200)
GPIO.add_event_detect(BUTTON2_GPIO, GPIO.RISING, callback=button2_callback, bouncetime=200)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting program")
finally:
    GPIO.cleanup()