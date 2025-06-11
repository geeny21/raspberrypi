'''
i2c Text LCD
주소 : 0x27
화면에 'hello' 출력 후 5초 대기
'''
from RPLCD.i2c import CharLCD
import time

# I2C 주소는 대부분 0x27 또는 0x3F (i2cdetect -y 1 명령어로 확인 가능)
lcd = CharLCD('PCF8574', 0x27)

lcd.write_string('hello')
time.sleep(5)
lcd.clear()  # LCD 화면을 지웁니다.
lcd.write_string('goodbye')
time.sleep(5)
lcd.clear()  # LCD 화면을 지웁니다.
lcd.close(clear=True)  # LCD를 닫고 화면을 지웁니다.

