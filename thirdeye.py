#Anything needed to read the screen

import config
from PIL import Image
from PIL import ImageGrab
from win32gui import FindWindow, GetWindowRect
import ppadb
from ppadb.client import Client
import ppadb.application 
import os
import subprocess
import numpy
#User needs binary Tesseract installed. CV2 as well
from pytesseract import *
import cv2

pytesseract.tesseract_cmd = config.tesseract_cmd
p = subprocess.Popen("tasklist", stdout=subprocess.PIPE)

#Get Connection
def connect_to_bluestacks():
    
    os.system("adb kill-server")
    os.system("adb start-server")
    adb = Client(host='127.0.0.1', port=5037)

    devs = adb.devices()
    if len(devs) == 0:
        print("Bluestacks can't connect! Make sure you have ADB debugging enabled in Bluestacks' settings.")
        quit()
    return devs[0]


#Taking a screenshot
def ss(emu_instance):
    image = emu_instance.screencap()
    with open(config.tmp_ss_path, 'wb') as f:
        f.write(image)
    f.close()

def get_ss(rect=None, show=False):
    img = cv2.imread(config.tmp_ss_path)
    if rect != None:
        img = img[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
    if show:
        cv2.imshow("Screenshot", img)
        cv2.waitKey(0)
    return img

def read(rect=None, path=config.tmp_ss_path):
    text = pytesseract.image_to_string(get_ss(rect))
    return text

def is_img_in_ss(img, rect=None, show_process=False): #Does not work
    ss = get_ss(rect)
    result = cv2.matchTemplate(img, ss, cv2.TM_SQDIFF_NORMED)

    if show_process:
        # We want the minimum squared difference
        mn,_,mnLoc,_ = cv2.minMaxLoc(result)

        # Draw the rectangle:
        # Extract the coordinates of our best match
        MPx,MPy = mnLoc

        # Step 2: Get the size of the template. This is the same size as the match.
        trows,tcols = img.shape[:2]

        # Step 3: Draw the rectangle on large_image
        cv2.rectangle(ss, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

        # Display the original image with the rectangle around the match.
        cv2.imshow('output',ss)

        # The image is only displayed if we call this
        cv2.waitKey(0)

    print(result)
    if result:
        return True
    else:
        return False

def where_are_we():
    #Menu - Main Menu
    play_btn_img = cv2.imread('img/play_btn.png')
    if is_img_in_ss(play_btn_img, show_process=True):
        return "main_menu"


    