import pyautogui
from oyunac import*
import cv2

yumruk_cascade = cv2.CascadeClassifier('fist.xml')

def tanimla(frame):
    global det
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    yumruk = yumruk_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in yumruk:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        det = 1
    return frame

video_capture = cv2.VideoCapture(0)

open_game(browser='windows-default', url='http://apps.thecodepost.org/trex/trex.html')

while True:
    _, frame = video_capture.read()
    det = 0
    canvas = tanimla(frame)
    cv2.imshow('Oyun', canvas)
    cv2.waitKey(1)
    if (det == True):
        pyautogui.press("space")
