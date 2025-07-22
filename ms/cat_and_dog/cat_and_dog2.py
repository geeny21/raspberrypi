'''
 티쳐블 머신으로 학습시킨 고양이와 개 구분 에제
 웹캠으로 입력
 고양이이면 먹이통 열기 (서보모터 : 180도)
 아니면 먹이통 닫기 (서보모터 : 0도)

 배경이 고양이나 개로 인식할 수 있다. 
 학습할 때 배경도 추가 학습시키면 이 문제를 해결할 수 있다. 
'''
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import RPi.GPIO as GPIO
import time
import playsound
from gtts import gTTS
import os

# 음성 출력 함수
def speak(text):
    # gTTS로 텍스트를 음성으로 변환 (lang="ko" 한글 설정)
    tts = gTTS(text=text, lang="ko")
    filename = "temp_tts.mp3"
    tts.save(filename)
    # mp3 파일 재생
    playsound.playsound(filename)
    #os.system("mpg123 "+filename)

    # 재생 후 임시 파일 삭제
    os.remove(filename)


# def map(value, from_min, from_max, to_min, to_max):
#     """주어진 범위에서 값을 다른 범위로 매핑하는 함수"""
#     return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min      

def servo(angle):
    if angle < 0 or angle > 180:
        print("Angle must be between 0 and 180 degrees.")
        return   # 잘못된 각도 입력 처리

    duty_cycle = (angle / 18) + 2.5  # 각도를 듀티 사이클로 변환
    #duty_cycle = map(angle, 0, 180, 5, 10)  # 각도를 듀티 사이클로 변환 (5% ~ 10%)
    print(f'Setting servo to {angle} degrees (Duty Cycle: {duty_cycle}%)')
    pwm.ChangeDutyCycle(duty_cycle)  # 듀티 사이클 변경
    #time.sleep(1)  # 1초 동안 유지

servo_pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz 주파수로 PWM 객체 생성
pwm.start(0)  # PWM 신호를 0% 듀티 사이클로 시작

food_state = 0  # 고앙이 먹이통 닫힘 상태
servo(0)       # 고양이 먹이통 닫힘

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

try :
    filedir="/home/pi/work/raspberrypi/ms/cat_and_dog/"

    print("모델 읽는 중")
    # Load the model
    model = load_model(filedir+"keras_model.h5", compile=False)

    # Load the labels
    class_names = open(filedir+"labels.txt", "r").readlines()
    print("모델 읽기 완료")
except Exception as e:
    print(f"에러 발생: {e}")


# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)
try :
    while True:
        # Grab the webcamera's image.
        ret, image = camera.read()

        # Resize the raw image into (224-height,224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Show the image in a window
        cv2.imshow("Webcam Image", image)

        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predicts the model
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
        
        if class_name[2:].strip() == "cat" and food_state==0 :
            speak("안녕 고양아")
            food_state  = 1
            servo(180)
            time.sleep(2)
        elif class_name[2:].strip() != "cat" and food_state== 1:
            speak("고양이 먹이 뿐입니다.")
            food_state = 0
            servo(0)
            time.sleep(2)


        # Listen to the keyboard for presses.
        keyboard_input = cv2.waitKey(1)

        # 27 is the ASCII for the esc key on your keyboard.
        if keyboard_input == 27:
            break

    camera.release()
    cv2.destroyAllWindows()
except KeyboardInterrupt:
    print("Keyboard interrupt")
finally :
    pwm.stop()
    del pwm
    GPIO.cleanup()  # GPIO 설정 초기화  
    print("GPIO cleanup completed.") 
