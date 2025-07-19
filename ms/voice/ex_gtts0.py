'''
pip install gtts
pip install playsound==1.2.2
sudo apt-get install python3-gi

sudo apt install mpg123 (playsound의 의존성)
'''
from gtts import gTTS
#import playsound
import os

def speak(text):
    # gTTS로 텍스트를 음성으로 변환 (lang="ko" 한글 설정)
    tts = gTTS(text=text, lang="ko")
    filename = "temp_tts.mp3"
    tts.save(filename)
    # mp3 파일 재생
    #playsound.playsound(filename)
    os.system("mpg123 "+filename)

    # 재생 후 임시 파일 삭제
    os.remove(filename)

# 예시: 한글 문장 읽기
speak("파이썬으로 음성 합성 예제를 실행합니다.")


