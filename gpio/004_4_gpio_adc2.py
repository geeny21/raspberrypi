'''
gpiozero를 이용한 MCP3008 ADC 사용 예제
CH0,CH1의 입력값이 0.5 이상이면 LED를 켜고, 그렇지 않으면 LED를 끄는 예제
'''
from gpiozero import MCP3008
import RPi.GPIO as GPIO
import time

led_pin = [17, 27]

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

# MCP3008 ADC 설정
# MCP3008은 SPI 통신을 사용하여 Raspberry Pi와 연결됩니다.
adc_ch0 = MCP3008(channel=0)  # 채널 0
adc_ch1 = MCP3008(channel=1)  # 채널 1

while True:
    print(f"CH0: {adc_ch0.value:.3f}, CH1: {adc_ch1.value:.3f}")
    if adc_ch0.value > 0.5:
        GPIO.output(led_pin[0], True)
        #print(f'Led {led_pin[0]} on')
    else:
        GPIO.output(led_pin[0], False)
        #print(f'Led {led_pin[0]} off')
    if adc_ch1.value > 0.5:
        GPIO.output(led_pin[1], True)
        #print(f'Led {led_pin[1]} on')
    else:
        GPIO.output(led_pin[1], False)
        #print(f'Led {led_pin[1]} off')
    
    #time.sleep(0.5)
