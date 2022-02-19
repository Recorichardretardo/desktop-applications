from PIL import Image, ImageGrab
Image.MAX_IMAGE_PIXELS = None
from pynput import keyboard
import time
from datetime import datetime
from threading import Thread
from pynput.keyboard import Listener

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='a'), keyboard.KeyCode(char='d')},
    {keyboard.Key.shift, keyboard.KeyCode(char='A'), keyboard.KeyCode(char='D')},
    {keyboard.Key.shift, keyboard.KeyCode(char='E')},
]

i = 1
current = set()




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
#with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    #listener.join()

lis  =  keyboard.Listener(on_press=on_press, on_release=on_release)
lis.start()
lis.join()
# with Listener(on_press=on_press) as ls:
#     time.sleep(1)
#     def time_out(period_sec: int):
#         time.sleep(period_sec)  # Listen to keyboard for period_sec seconds
#         #ls.stop()

#     Thread(target=time_out, args=(5.0,)).start()
#     ls.join()