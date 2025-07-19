'''
playsound() 에서 오류가 발생한다. 
가상환경이 아닌 곳에서 다음 실행 후 재부팅
sudo apt-get install python3-gi python3-gi-cairo libgirepository1.0-dev libcairo2-dev libgstreamer1.0-0 gstreamer1.0-dev gstreamer1.0-tools gir1.2-gtk-3.0

'''
import RPi.GPIO as GPIO
import time
import speech_recognition as sr
from word2number import w2n
from gtts import gTTS
import playsound
import os

def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename = "temp_gtts.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    #os.system("mpg123 " + filename)
    os.remove(filename)

def servo(angle):
    if angle < 0 or angle > 180:
        speak("각도는 0도에서 180도 사이여야 합니다.")
        return
    duty_cycle = (angle / 18) + 2.5
    speak(f"{angle}도로 이동합니다.")
    pwm.ChangeDutyCycle(duty_cycle)

servo_pin = 21

recognizer = sr.Recognizer()
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

with sr.Microphone() as source:
    while True:
        speak("숫자를 말하세요. 종료하려면 '종료'라고 말씀하세요.")
        print("숫자를 말하세요. (종료하려면 '종료'라고 말하세요)")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='ko-KR')
            print("인식된 음성:", text)
            if text in ["종료", "끝", "그만"]:
                speak("프로그램을 종료합니다.")
                print("프로그램을 종료합니다.")
                break
            try:
                number = w2n.word_to_num(text)
            except Exception:
                speak("숫자를 정확히 말씀해 주세요.")
                print("에러: 숫자 인식 실패")
                continue
            print("인식한 숫자값:", number)
            if number < 0 or number > 180:
                speak("각도는 0도에서 180도 사이여야 합니다.")
                print("각도는 0에서 180 사이여야 합니다.")
                continue
            servo(number)
            time.sleep(1)
        except Exception as e:
            speak("에러가 발생했습니다.")
            print("에러:", e)
        except KeyboardInterrupt:
            speak("프로그램을 종료합니다.")
            print("프로그램을 종료합니다.")
            break

pwm.stop()
del pwm
GPIO.cleanup()
print("GPIO cleanup completed.")
