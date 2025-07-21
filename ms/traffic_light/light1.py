'''
RGB LED Traffic Light Control
점등 상황 사운드로 안내
'''

import time
import RPi.GPIO as GPIO
from playsound import playsound
from gtts import gTTS
import os

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
            playsound('red.mp3')
            time.sleep(5)  # Red light duration

            # Green light
            GPIO.output(LED_R, GPIO.LOW)
            GPIO.output(LED_G, GPIO.HIGH)
            GPIO.output(LED_Y, GPIO.LOW)
            print("Green Light ON")
            playsound('green.mp3')
            time.sleep(5)  # Green light duration

            # Yellow light
            GPIO.output(LED_R, GPIO.LOW)
            GPIO.output(LED_G, GPIO.LOW)
            GPIO.output(LED_Y, GPIO.HIGH)
            print("Yellow Light ON")
            playsound('yellow.mp3')
            time.sleep(2)  # Yellow light duration

    except KeyboardInterrupt:
        print("Traffic light control stopped.")
    finally:
        GPIO.cleanup()
        os.remove("red.mp3")
        os.remove("green.mp3")
        os.remove("yellow.mp3")

if __name__ == "__main__":
    # gTTS를 이용하여 음성 파일을 생성한다.
    text = "신호등이 작동합니다."
    text = "빨간불입니다. 건너지 마십시요."
    tts = gTTS(text=text, lang='ko')  # 한국어 설정
    tts.save("red.mp3")
    text = "초록불입니다. 신속히 건너십시요."
    tts = gTTS(text=text, lang='ko')  # 한국어 설정
    tts.save("green.mp3")
    text = "노란불입니다. 진입하지 마십시요."
    tts = gTTS(text=text, lang='ko')  # 한국어 설정
    tts.save("yellow.mp3")
    
    print("Starting traffic light control...")
    traffic_light_cycle()
    print("Traffic light control finished.")