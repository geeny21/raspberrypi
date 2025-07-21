'''
tkinter를 이용한 3색 LED 버튼 토글 GUI
LED와 연동
'''
import tkinter as tk
import RPi.GPIO as GPIO

LED_R = 22
LED_G = 27
LED_Y = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_Y, GPIO.OUT)

GPIO.output(LED_R, GPIO.LOW)
GPIO.output(LED_G, GPIO.LOW)
GPIO.output(LED_Y, GPIO.LOW)

# 각 버튼의 ON/OFF 상태 변수
red_on = False
green_on = False
yellow_on = False

def toggle_red():
    global red_on
    red_on = not red_on
    GPIO.output(LED_R, red_on)
    if red_on:
        btn_red.config(
            text="빨강 ON",
            bg="red",
            fg="white",
            relief="sunken"
        )
    else:
        btn_red.config(
            text="빨강 OFF",
            bg="lightgray",
            fg="black",
            relief="raised"
        )

def toggle_green():
    global green_on
    green_on = not green_on
    GPIO.output(LED_G, green_on)
    if green_on:
        btn_green.config(
            text="초록 ON",
            bg="green",
            fg="white",
            relief="sunken"
        )
    else:
        btn_green.config(
            text="초록 OFF",
            bg="lightgray",
            fg="black",
            relief="raised"
        )

def toggle_yellow():
    global yellow_on
    yellow_on = not yellow_on
    GPIO.output(LED_Y, yellow_on)
    if yellow_on:
        btn_yellow.config(
            text="노랑 ON",
            bg="gold",
            fg="white",
            relief="sunken"
        )
    else:
        btn_yellow.config(
            text="노랑 OFF",
            bg="lightgray",
            fg="black",
            relief="raised"
        )

root = tk.Tk()
root.title("3색 LED 버튼 토글 GUI (변수 관리)")

btn_red = tk.Button(
    root,
    text="빨강 OFF",
    width=15,
    height=3,
    bg="lightgray",
    relief="raised",
    command=toggle_red
)
btn_red.grid(row=0, column=0, padx=12, pady=25)

btn_green = tk.Button(
    root,
    text="초록 OFF",
    width=15,
    height=3,
    bg="lightgray",
    relief="raised",
    command=toggle_green
)
btn_green.grid(row=0, column=1, padx=12, pady=25)

btn_yellow = tk.Button(
    root,
    text="노랑 OFF",
    width=15,
    height=3,
    bg="lightgray",
    relief="raised",
    command=toggle_yellow
)
btn_yellow.grid(row=0, column=2, padx=12, pady=25)

root.mainloop()
