#!/usr/bin/python3
# snap.py  can't believe I can't find this...
# major reference -- don't know if it's printed etc:
#   pi@mc24b: ~/py/pirfsm/button-sleep.py
 
import os, sys, time
from time import sleep
import datetime
#from picamera import PiCamera
#camera = PiCamera()
import picamera
 
def getFileName():   # create new Filename from date and time
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")

def snap(filename):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        sleep(2) # Camera warm-up time
        camera.start_preview()
        camera.capture(filename)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "mysnap.jpg"
    print(filename)
    snap(filename)

"""
# no resolution specified. Gives me the max 1920x1080.
camera.resolution = (1024, 768)
camera.resolution = (640, 480)
camera.resolution = (512, 384)
camera.resolution = (256, 192)
camera.resolution = (320, 240)
"""


