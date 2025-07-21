'''
pip instll coqui-tts
동작 안됨
'''
# from TTS.api import TTS
# import os

# tts = TTS(model_name="tts_models/ko/kss/tacotron2-DDC", progress_bar=False, gpu=False)
# tts.tts_to_file(text="안녕하세요. 자연스러운 TTS 예제입니다.", file_path="output.wav")

# os.system('aplay output.wav')  # aplay를 사용하여 음성 재생

'''
git clone https://github.com/myshell-ai/MeloTTS.git
cd MeloTTS
pip install .
pip list | grep melo
'''
from melo.api import TTS
import os
model = TTS(language='KR', device='cpu')
model.tts_to_file("안녕하세요! 오늘은 날씨가 정말 좋네요.", model.hps.data.spk2id['KR'], 'kr.wav')
os.system('aplay kr.wav')  # aplay를 사용하여 음성 재생

