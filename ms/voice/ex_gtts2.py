from gtts import gTTS
import playsound
import speech_recognition as sr
import os
import time

def speak(text):
    tts = gTTS(text=text, lang="ko")
    filename = "temp_tts.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

recognizer = sr.Recognizer()
audio = ""

speak("파이썬으로 음성 합성 예제를 실행합니다.")

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)  # Noise 환경 잡아주기
    while True:
        speak("명령을 입력하세요.")  # 안내멘트
        time.sleep(0.7) # 소리가 완전히 끝난 뒤 실제 녹음 시작되도록 약간 더 쉬기

        # 1차 버퍼 비우기(짧은 시간 샘플링)
        print("==> 버퍼 정리용 입력 청취")
        try:
            recognizer.listen(source, timeout=1, phrase_time_limit=1) # 1초 버리기
        except sr.WaitTimeoutError:
            pass
        
        if audio != "" :
            audio = ""
            continue

        print("==> 음성 명령 입력 대기 중 …")
        audio = recognizer.listen(source) # 본격적으로 음성 명령 입력 받기
        print("==> 음성 명령 수신됨.")
        text =""
        try:
            text = recognizer.recognize_google(audio, language='ko-KR')
            
            audio = ""

            print("인식된 음성:", text)
            speak("당신이 말씀하신 명령은 " + text + "입니다.")

            if text in ["종료", "끝", "그만"]:
                speak("프로그램을 종료합니다.")
                print("프로그램을 종료합니다.")
                break

            text = ""

        except Exception as e:
            speak("음성을 인식하지 못했습니다. 다시 시도해주세요.")
            print("에러:", e)
        except KeyboardInterrupt:
            speak("프로그램을 종료합니다.")
            print("프로그램을 종료합니다.")
            break
