from PIL import Image, ImageGrab
Image.MAX_IMAGE_PIXELS = None
from pynput import keyboard
import time
from datetime import datetime

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='a'), keyboard.KeyCode(char='d')},
    {keyboard.Key.shift, keyboard.KeyCode(char='A'), keyboard.KeyCode(char='D')},
    {keyboard.Key.shift, keyboard.KeyCode(char='E')},
]

i = 1
current = set()

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


def printScreen():
    print("print screen")

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            if keyboard.KeyCode(char='E') in current:
                print("stop execution")
                return False
            execute()
           

def on_release(key):
    try:
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.remove(key)
    except Exception:
        pass

    if key == keyboard.Key.esc:
        return False
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()