from PIL import Image, ImageGrab
Image.MAX_IMAGE_PIXELS = None
from datetime import datetime
from pynput import keyboard

i = 1
def execute():
    global i
    number = i
    date = datetime.now().strftime("%Y-%m-%dT%H_%M_%S_%f")
    print("date :",date)
    fileName = f"image_{date}_{number}.png"
    try:
        print("fileName : ",fileName)
        #img = ImageGrab.grab(bbox=(10,10,500,500))
        img = ImageGrab.grab()
        #img.show()
        img.save(f"image_{date}_{number}.png")
    except Exception as e:
        print('print secree error : {0}'.format(e))
    print("count : ",number)
    i = i+1


def function_1():
    print('Function 1 activated')

def quitExecution():
    quit()

with keyboard.GlobalHotKeys({
        '<shift>+a+r': execute,
        '<shift>+e+t': execute,
        '<shift>+q+t': quitExecution}) as h:
    h.join()