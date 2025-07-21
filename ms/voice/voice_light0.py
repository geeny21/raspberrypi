'''
음성으로 LED 제어
'''
import RPi.GPIO as GPIO
import speech_recognition as sr
import time


GPIO.setmode(GPIO.BCM)

LED_R = 22
LED_G = 27
LED_Y = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_Y, GPIO.OUT)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        print("명령을 말하세요. (종료하려면 '종료'라고 말하세요)")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='ko-KR')
            #text = recognizer.recognize_google(audio, language='en-US')
            print("인식된 음성:", text)
            if text in ["종료", "끝", "그만"]:
                print("프로그램을 종료합니다.")
                break
            elif text in ["빨강 켜", "빨간 켜", "빨간불 켜"]:
                GPIO.output(LED_R, GPIO.HIGH)
                print("빨간불 켜짐")
            elif text in ["초록 켜", "초록불 켜"]:
                GPIO.output(LED_G, GPIO.HIGH)
                print("초록불 켜짐")
            elif text in ["노랑 켜", "노란 켜", "노란불 켜"]:
                GPIO.output(LED_Y, GPIO.HIGH)
                print("노란불 켜짐")
            elif text in ["빨강 꺼", "빨간 꺼", "빨간불 꺼"]:
                GPIO.output(LED_R, GPIO.LOW)
                print("빨간불 꺼짐")
            elif text in ["초록 꺼", "초록불 꺼"]:
                GPIO.output(LED_G, GPIO.LOW)
                print("초록불 꺼짐")
            elif text in ["노랑 꺼", "노란 꺼", "노란불 꺼"]:
                GPIO.output(LED_Y, GPIO.LOW)
                print("노란불 꺼짐")
            elif text in ["모두 켜기", "모두 켜"]:
                GPIO.output(LED_R, GPIO.HIGH)
                GPIO.output(LED_G, GPIO.HIGH)
                GPIO.output(LED_Y, GPIO.HIGH)
                print("모든 불 켜짐")
            elif text in ["모두 끄기", "모두 꺼"]:
                GPIO.output(LED_R, GPIO.LOW)
                GPIO.output(LED_G, GPIO.LOW)
                GPIO.output(LED_Y, GPIO.LOW)
                print("모든 불 꺼짐")
            else:
                print("알 수 없는 명령입니다.")
        except Exception as e:
            print("에러:", e)
        except KeyboardInterrupt:
            print("프로그램을 종료합니다.")
            break   