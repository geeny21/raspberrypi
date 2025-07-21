'''
RGB LED Traffic Light Control
'''

import time
import RPi.GPIO as GPIO

LED_R = 22
LED_G = 27
LED_Y = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_Y, GPIO.OUT)

def traffic_light_cycle():
    try:
        while True:
            # Red light
            GPIO.output(LED_R, GPIO.HIGH)
            GPIO.output(LED_G, GPIO.LOW)
            GPIO.output(LED_Y, GPIO.LOW)
            print("Red Light ON")
            time.sleep(5)  # Red light duration

            # Green light
            GPIO.output(LED_R, GPIO.LOW)
            GPIO.output(LED_G, GPIO.HIGH)
            GPIO.output(LED_Y, GPIO.LOW)
            print("Green Light ON")
            time.sleep(5)  # Green light duration

            # Yellow light
            GPIO.output(LED_R, GPIO.LOW)
            GPIO.output(LED_G, GPIO.LOW)
            GPIO.output(LED_Y, GPIO.HIGH)
            print("Yellow Light ON")
            time.sleep(2)  # Yellow light duration

    except KeyboardInterrupt:
        print("Traffic light control stopped.")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    print("Starting traffic light control...")
    traffic_light_cycle()
    print("Traffic light control finished.")