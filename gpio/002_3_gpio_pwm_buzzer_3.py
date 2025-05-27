'''
수동 부저로 PWM 소리 내기
도래미파솔라시도 연수
부저 핀 : GPIO28

주파수
C (do) - 261.63 Hz
D (re) - 293.66 Hz
E (mi) - 329.63 Hz
F (fa) - 349.23 Hz
G (sol) - 392.00 Hz
A (la) - 440.00 Hz
B (ti) - 493.88 Hz
C5 (do high) - 523.25 Hz

'''
import RPi.GPIO as GPIO
import time

# 1. 음계별 주파수 정의 (옥타브4 기준, Hz)
NOTE_FREQ = {
    'C': 261.63,    # 도
    'D': 293.66,    # 레
    'E': 329.63,    # 미
    'F': 349.23,    # 파
    'G': 392.00,    # 솔
    'A': 440.00,    # 라
    'B': 493.88,    # 시
    'C5': 523.25    # 높은 도
}

# 2. 연주할 음계 리스트
melody = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C5']

# 3. 부저가 연결된 GPIO 핀 번호
BUZZER_PIN = 28

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 440)  # 초기 주파수 440Hz로 PWM 객체 생성

try:
    for note in melody:
        freq = NOTE_FREQ[note]
        pwm.ChangeFrequency(freq)
        pwm.start(50)         # 50% 듀티 사이클로 시작
        time.sleep(0.5)       # 0.5초 연주
        pwm.stop()
        time.sleep(0.1)       # 음 사이 간격
        
except KeyboardInterrupt:
    print("Key interrupt")
except :
    print("An error occurred or program interrupted.")
finally:
    pwm.stop()        # PWM 중지
    del pwm             # PWM 객체 삭제
    GPIO.cleanup()    # GPIO 리소스 정리
print('Program end')  # 프로그램 종료 메시지 출력
