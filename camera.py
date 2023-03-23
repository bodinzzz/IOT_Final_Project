import cv2
import pyzbar.pyzbar as pyzbar
import time
import picamera
from medicine_dispenser import angle_to_duty_cycle, test

def take_picture():
    camera = picamera.PiCamera()
    time.sleep(5)
    camera.capture('test.png')

    image = cv2.imread("test.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    texts = pyzbar.decode(gray)
    for text in texts:
        tt = text.data.decode("utf-8")
        text(tt)