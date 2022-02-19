from PIL import Image, ImageGrab
Image.MAX_IMAGE_PIXELS = None
from datetime import datetime
from pynput import keyboard


    
def function_1():
    print('Function 1 activated')

def function_2():
    quit()

with keyboard.GlobalHotKeys({
        '<shift>+a+r': function_1,
        '<shift>+e+t': function_1,
        '<shift>+q+t': function_2}) as h:
    h.join()