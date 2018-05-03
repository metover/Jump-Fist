import pyautogui
import webbrowser
import cv2

yumruk_cascade = cv2.CascadeClassifier('fist.xml')


def tanimla(goruntu):
    global det
    gray = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    yumruk = yumruk_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in yumruk:
        cv2.rectangle(goruntu, (x, y), (x + w, y + h), (255, 0, 0), 2)
        det = 1
    return goruntu


def open_game(browser, url):
    return webbrowser.get(browser).open(url)


video_capture = cv2.VideoCapture(0)

open_game(browser='windows-default',
          url='http://apps.thecodepost.org/trex/trex.html')

while True:
    _, frame = video_capture.read()
    det = 0
    canvas = tanimla(frame)
    cv2.imshow('Oyun', canvas)
    cv2.waitKey(1)
    if (det == 1):
        pyautogui.press("space")
