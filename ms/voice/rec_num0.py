'''
# This script recognizes spoken numbers in Korean and converts them to numerical values.
# It uses the SpeechRecognition library for audio input and the word2number library for number conversion.
# Make sure to install the required libraries before running the script:
pip install word2number
pip install SpeechRecognition

sudo apt install portaudio19-dev python3-pyaudio
pip install PyAudio
sudo apt-get install flac

'''
import speech_recognition as sr
from word2number import w2n

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        print("숫자를 말하세요. (종료하려면 '종료'라고 말하세요)")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='ko-KR')
            print("인식된 음성:", text)
            if text in ["종료", "끝", "그만"]:
                print("프로그램을 종료합니다.")
                break
            number = w2n.word_to_num(text)
            print("인식한 숫자값:", number)
        except Exception as e:
            print("에러:", e)
        except KeyboardInterrupt:
            print("프로그램을 종료합니다.")
            break   