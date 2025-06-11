'''
MCP3008
CH0
CH1
SPI 통신 (/dev/spidev0.0)
'''

import spidev
import time
#import RPi.GPIO as GPIO

delay = 0.5
adc_channel0 = 0  # MCP3008의 CH0 채널을 사용
adc_channel1 = 1  # MCP3008의 CH1 채널을 사용

spi = spidev.SpiDev()
spi.open(0, 0)  # SPI 버스 0, 디바이스 0
#spi.max_speed_hz = 1350000  # SPI 최대 속도 설정 (1.35MHz)
spi.max_speed_hz = 1000000

# MCP3008의 channel 채널을 읽어오는 함수
def read_adc(channel):
    if channel < 0 or channel > 7:
        raise ValueError("ADC channel must be between 0 and 7")
    
    # MCP3008의 SPI 통신을 통해 ADC 값을 읽어옴
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    result = ((adc[1] & 3) << 8) + adc[2]
    return result   

try:
    while True:
        adc_value = read_adc(adc_channel0)  # ADC 값 읽기
        print(f"ADC Channel {adc_channel0} Value: {adc_value}")  # ADC 값 출력

        
        adc_value = read_adc(adc_channel1)  # ADC 값 읽기
        print(f"ADC Channel {adc_channel1} Value: {adc_value}")  # ADC 값 출력

        time.sleep(delay)  # 지정된 시간만큼 대기
        print("-" * 30)  # 구분선 출력

except KeyboardInterrupt:   
    print("\nExiting program")

finally:
    spi.close()
    print("SPI communication closed")
    
# GPIO.cleanup()  # GPIO 설정을 초기화 (필요시 사용)
print("Program finished")