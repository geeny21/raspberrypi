'''
gpiozero를 이용한 MCP3008 ADC 사용 예제
최대값 1
최소값 0
MCP3008은 SPI 통신을 사용하여 Raspberry Pi와 연결됩니다.
MCP3008 채널 0과 1의 값을 읽어 출력하는 예제
'''
from gpiozero import MCP3008
import time

adc_ch0 = MCP3008(channel=0)  # 채널 0
adc_ch1 = MCP3008(channel=1)  # 채널 1

while True:
    print(f"CH0: {adc_ch0.value:.3f}, CH1: {adc_ch1.value:.3f}")
    time.sleep(0.5)
