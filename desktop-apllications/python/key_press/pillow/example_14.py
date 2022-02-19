from PIL import Image, ImageGrab
Image.MAX_IMAGE_PIXELS = None
from pynput import keyboard
import time
from datetime import datetime

i = 1

def printScreen():
    global i
    number = i
    t1 = time.time()
    date = datetime.now().strftime("%Y-%m-%dT%H_%M_%S_%f")
    print("date :",date)
    img = ImageGrab.grab(bbox=(10,10,500,500))
    #img.show()
    img.save(f"image_{date}_{number}.png")
    t2 = time.time()
    print("The passing time",(t2-t1))
    print("The passing time",number)
    print("came here",number)
    time.sleep(0.5)
    i = i+1
    
def on_press(key):
    try:
        #print('Alphanumeric key pressed: {0} '.format(key.char))
        if(key.char == '^'):
            print('Alphanumeric key pressed: {0} '.format(key.char))
            printScreen()
    except AttributeError:
        #print('special key pressed: {0}'.format(key))
        pass

def on_release(key):
    #print('Key released: {0}'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


