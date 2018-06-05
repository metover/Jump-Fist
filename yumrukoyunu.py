# Bu Calisma Mert Cobanoglu tarafından yazılmıstır. 

import webbrowser
import pyautogui
import cv2

yumruk_cascade = cv2.CascadeClassifier('fist.xml') # Yumruk tanımlama için 

def browser_oyun(browser, url): # Browser aracılığyla oynanılacak oyunu açar.
    return webbrowser.get(browser).open(url)

def tanimla(goruntu): # Goruntuyu alıp işleyecek fonk, aynı zamanda tanımlanan alana bir çerçeve çizer.
    global det
    gray = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    yumruk = yumruk_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in yumruk:
        cv2.rectangle(goruntu, (x, y), (x + w, y + h), (255, 0, 0), 2)
        det = 1
    return goruntu

video_capture = cv2.VideoCapture(0)

# Burada bir hata alıyorsanız webbrowser kütüphanesinin dokümantasyonuna gözatın, kullandığınız browseri fonksiyon içerisinde yazabilirsiniz.
browser_oyun(browser='windows-default',url='http://apps.thecodepost.org/trex/trex.html')

while True:
    _, frame = video_capture.read()
    det = 0
    canvas = tanimla(frame)
    cv2.imshow('Yumruk Oyunu - Metover', canvas)
    cv2.waitKey(1)
    if (det == 1):
        pyautogui.press("space")
