'''
gpio17에 led 연결
2초 단위 점별 5회 반복하고 프로그램 종료
'''
import RPi.GPIO as GPIO
import time

led_pin = 17

try :
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(led_pin, GPIO.OUT)

    for i in range(5):
        GPIO.output(led_pin, True)
        print('Led on')

        time.sleep(1.0)

        GPIO.output(led_pin, False)
        print('Led off')

        time.sleep(1.0)
except KeyboardInterrupt :
    print("Key interrupt")
except Exception as e:
    print(f"An error occurred: {e}")
finally :
    GPIO.cleanup()
    print('clean up done')
print('Program end')