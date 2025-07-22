'''
파일의 사진이 개인지 고양이인지 구분하는 예제
파일에서 그림 읽기
'''
from keras.models import load_model
import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

try:
    filedir = "/home/pi/work/raspberrypi/ms/cat_and_dog/"
    print("모델 읽는 중")
    # Load the model
    model = load_model(filedir + "keras_model.h5", compile=False)
    # Load the labels
    class_names = open(filedir + "labels.txt", "r").readlines()
    print("모델 읽기 완료")
except Exception as e:
    print(f"에러 발생: {e}")

# Tkinter로 파일 오픈 다이얼로그 띄우기
root = tk.Tk()
root.withdraw()  # Tk 창 숨기기

file_path = filedialog.askopenfilename(
    title="이미지 파일을 선택하세요",
    #filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")]
)
# file_path = filedialog.askopenfilename(
#     title="이미지 파일을 선택하세요",
#     filetypes=[
#         ("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.JPG;*.JPEG;*.PNG;*.BMP"),
#         ("All Files", "*.*")
#     ]
# )


if not file_path:
    print("이미지 파일을 선택하지 않았습니다.")
    exit()

# 이미지 로드 및 전처리
image = cv2.imread(file_path)
if image is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 크기 조정(모델 입력크기 224x224)
image_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
cv2.imshow("Selected Image", image_resized)



# numpy array 변환 및 전처리
input_image = np.asarray(image_resized, dtype=np.float32).reshape(1, 224, 224, 3)
input_image = (input_image / 127.5) - 1

# 예측
prediction = model.predict(input_image)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# 결과 출력
print("Class:", class_name[2:].strip())
print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

print(type(class_name))
print(class_name)
while True:
    key = cv2.waitKey(1)  # 1ms마다 키 이벤트 체크
    if key == 27:         # ESC키 코드: 27
        break
cv2.destroyAllWindows()