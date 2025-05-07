'''
gpio17에 led 연결
점멸 비율 조정하여 밝기 변경
Ctrl+C 누르면 프로그램 종료
'''
import RPi.GPIO as GPIO
import time

led_pin = 17
d_time = 0.001
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

try :
    while True :
        GPIO.output(led_pin, True)
        #print('Led on')
        time.sleep(d_time*9)

        GPIO.output(led_pin, False)
        #print('Led off')
        time.sleep(d_time)

except KeyboardInterrupt :
    print("Key interrupt")
GPIO.cleanup()
print('Program end')