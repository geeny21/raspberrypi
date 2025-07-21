'''
음성으로 현재 시간을 알려주는 프로그램
12시 기준 - AM/PM 구분
'''
import time
import datetime
from gtts import gTTS
from playsound import playsound

def spaek_time():
    now = datetime.datetime.now()
    #current_time = now.strftime("%H시 %M분 %S초")
    current_time = now.strftime("%p %I시 %M분 %S초")
    print("현재 시간:", current_time)
    
    tts = gTTS(text=current_time, lang='ko')  # 한국어 설정
    tts.save("current_time.mp3")
    playsound("current_time.mp3")  # 음성 재생

if __name__ == "__main__":
    while True:
        spaek_time()
        #time.sleep(60)  # 1분마다 현재 시간 알림
        time.sleep(10)  # 테스트용으로 10초마다 알림