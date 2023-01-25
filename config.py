#Variables to change
tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe" #Absolute path to tesseract.exe

#Global variables
bluestack_port = 5555
tmp_ss_path = "tmp/screen.png"
#Adapted for 900x1600 portrait resolution on Bluestacks
#Code might not work if your resolution isn't set to that in the emulator's settings
screen_zones = {
    'menu_nav_bar' : (0,1372, 900, 228),
    'menu_play_btn' : (344, 1218, 214, 125)
}