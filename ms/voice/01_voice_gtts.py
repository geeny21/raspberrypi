'''
gTTS를 이용한 음성 출력 예제
pip install gTTS
sudo apt install mpg321

pip install playsound==1.2.2

sudo apt install libcairo2-dev pkg-config python3-dev
sudo apt install libgirepository1.0-dev gir1.2-gtk-4.0

sudo apt install libgirepository1.0-dev gir1.2-glib-2.0

sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-4.0 \
libgirepository1.0-dev libcairo2-dev pkg-config python3-dev \
gstreamer1.0-tools gstreamer1.0-plugins-base gstreamer1.0-plugins-good

sudo apt install mpg321

sudo apt install python3-gi
sudo apt install gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0
pip install pygobject

음성이 기계음
'''
from gtts import gTTS
from playsound import playsound
#from os.path import expanduser
import os

text = "오늘은 매우 더운 날입니다. "
tts = gTTS(text=text, lang='ko')  # 한국어 설정
tts.save("hello.mp3")
os.system('mpg123 hello.mp3')  # mpg123를 사용하여 음성 재생

text = "Today is a very hot day. Please take care of your health."
tts = gTTS(text=text, lang='en')  # 영어 설정
tts.save("hello.mp3")
#playsound('/home/pi/work/hello.mp3')
#playsound(expanduser('~/work/hello.mp3'))
os.system('mpg123 hello.mp3')  # mpg123를 사용하여 음성 재생



text = "건강 유의하세요."
tts = gTTS(text=text, lang='ko')  # 한국어 설정
tts.save("hello1.mp3")
os.system('mpg123 hello.mp3')  # mpg123를 사용하여 음성 재생

text = "Today is a very hot day. Please take care of your health."
tts = gTTS(text=text, lang='en')  # 영어 설정
tts.save("hello1.mp3")
#playsound('/home/pi/work/hello.mp3')
#playsound(expanduser('~/work/hello.mp3'))
os.system('mpg123 hello1.mp3')  # mpg123를 사용하여 음성 재생