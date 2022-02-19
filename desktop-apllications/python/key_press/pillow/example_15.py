from PIL import Image, ImageGrab
Image.MAX_IMAGE_PIXELS = None
from pynput import keyboard
import time
from datetime import datetime

# The key combination to check
COMBINATIONS = [
     #{keyboard.KeyCode(char='a'),keyboard.KeyCode(char='r')}, # a + r
     #{keyboard.Key.shift, keyboard.KeyCode(char='p'),keyboard.KeyCode(char='s')}, 
     #{keyboard.Key.shift, keyboard.KeyCode(char='P'),keyboard.KeyCode(char='S')}, # shift + P + S
     {keyboard.Key.shift, keyboard.KeyCode(char='a')},
      {keyboard.Key.shift, keyboard.KeyCode(char='A')},
     {keyboard.Key.shift, keyboard.KeyCode(char='E')}, # shit + E to stop execution
]

# The currently active modifiers
current = set()

i = 1
def printScreen():
    try:
        global i
        number = i
        t1 = time.time()
        date = datetime.now().strftime("%Y-%m-%dT%H_%M_%S_%f")
        print("date :",date)
        #img = ImageGrab.grab(bbox=(10,10,500,500))
        #img.show()
        #img.save(f"image_{date}_{number}.png")
        t2 = time.time()
        print("The passing time",(t2-t1))
        print("The passing time",number)
        print("came here",number)
        time.sleep(0.5)
        i = i+1
    except Exception as e:
        print('print secree error : {0}'.format(e))

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            if keyboard.KeyCode(char='E') in current:
                print("stop execution")
                return False
            
            printScreen()

def on_release(key):
    try:
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.remove(key)

        #if key == keyboard.Key.esc:
            #return False
    except Exception:
        pass

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


