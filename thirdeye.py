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
#User needs binary Tesseract installed.
from pytesseract import *


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
    with open('tmp/screen.png', 'wb') as f:
        f.write(image)
    f.close()

def read(image, rect=None, path="tmp/screen.png"):
    img = Image.open(path)
    img = img.crop(rect)
    img.show()
    text = pytesseract.image_to_string(img)
    return text