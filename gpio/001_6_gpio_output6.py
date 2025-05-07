'''
gpio17에 led 연결
10 단계로 점점 밝아 지도록 제어 <- sleep 시간 조정
test2
'''
import RPi.GPIO as GPIO
import time

led_pin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

try :
    while True :
        for t_high in range(0, 101) :
            GPIO.output(led_pin, True)
            time.sleep(t_high*0.0001)
            GPIO.output(led_pin, False)
            time.sleep( (100-t_high)*0.0001)
except KeyboardInterrupt :
    print('Key interrupt')            

GPIO.cleanup()
