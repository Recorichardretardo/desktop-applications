from PIL import Image, ImageGrab
Image.MAX_IMAGE_PIXELS = None
import keyboard
import time
from datetime import datetime


def is_true():
    if keyboard.is_pressed('^'):
        return bool(True)
    else:
        return bool(False)

i = 1
while True:
    try:
        if is_true():
            number = i
            t1 = time.time()
            date = datetime.now().strftime("%Y-%m-%dT%H_%M_%S_%f")
            print("date :",date)
            img = ImageGrab.grab(bbox=(10,10,500,500))
            #^img.show()
            #img.save(f"image_{date}_{number}.png")
            t2 = time.time()
            print("The passing time",(t2-t1))
            print("The passing time",number)
            i = i+1
            time.sleep(0.1)
        elif keyboard.is_pressed('q'):
            break
        else:
            pass
    except Exception as e:
        print(e)
        break





