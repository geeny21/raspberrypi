import Adafruit_MCP3008
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)  # BCM 핀 번호 모드 설정

# MCP3008 ADC 설정
#mcp = Adafruit_MCP3008.MCP3008(spi=Adafruit_MCP3008.SpiDev(0, 0))
mcp = Adafruit_MCP3008.MCP3008(clk=11, cs=8, miso=9, mosi=10)

# ADC 채널 설정
adc_channel0 = 0  # MCP3008의 CH0 채널을 사용
adc_channel1 = 1  # MCP3008의 CH1 채널을 사용
# 측정 주기 설정
delay = 0.5
# MCP3008의 channel 채널을 읽어오는 함수
def read_adc(channel):
    if channel < 0 or channel > 7:
        raise ValueError("ADC channel must be between 0 and 7")
    
    # MCP3008의 SPI 통신을 통해 ADC 값을 읽어옴
    return mcp.read_adc(channel)
try:
    while True:
        adc_value = read_adc(adc_channel0)  # ADC 값 읽기
        print(f"ADC Channel {adc_channel0} Value: {adc_value}")  # ADC 값 출력
        
        adc_value = read_adc(adc_channel1)  # ADC 값 읽기
        print(f"ADC Channel {adc_channel1} Value: {adc_value}")  # ADC 값 출력
        
        time.sleep(delay)  # 지정된 시간만큼 대기
        print("-" * 30)
except KeyboardInterrupt:
    print("\nExiting program")
finally:
    GPIO.cleanup()
    print("Program finished")
# No cleanup needed for Adafruit_MCP3008
# as it handles SPI communication automatically
# No GPIO cleanup needed as we are not using RPi.GPIO
# print("GPIO cleanup done")
# No GPIO cleanup needed as we are not using RPi.GPIO
print("Program finished")