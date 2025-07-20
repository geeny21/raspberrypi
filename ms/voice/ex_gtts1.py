'''
pip install gtts
pip install playsound==1.2.2
sudo apt-get install python3-gi

sudo apt install mpg123 (playsound의 의존성)
'''
from gtts import gTTS
import playsound
import speech_recognition as sr
import os

def speak(text):
    # gTTS로 텍스트를 음성으로 변환 (lang="ko" 한글 설정)
    tts = gTTS(text=text, lang="ko")
    filename = "temp_tts.mp3"
    tts.save(filename)
    # mp3 파일 재생
    playsound.playsound(filename)
    #os.system("mpg123 "+filename)

    # 재생 후 임시 파일 삭제
    os.remove(filename)

recognizer = sr.Recognizer()

# 예시: 한글 문장 읽기
speak("파이썬으로 음성 합성 예제를 실행합니다.")
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)  # Noise 환경 잡아주기 
    while True:
        speak("명령을 입력하세요.")
        print("==> 음성 명령 대기 중.")
        audio = recognizer.listen(source)
        print("==> 음성 명령 수신됨.")
        try:
            text = recognizer.recognize_google(audio, language='ko-KR')
            print("인식된 음성:", text)
            speak(text)

            if text in ["종료", "끝", "그만"]:
                speak("프로그램을 종료합니다.")
                print("프로그램을 종료합니다.")
                break

        except Exception as e:
            speak("에러가 발생했습니다.")
            print("에러:", e)
        except KeyboardInterrupt:
            speak("프로그램을 종료합니다.")
            print("프로그램을 종료합니다.")


