from PIL import Image, ImageGrab
Image.MAX_IMAGE_PIXELS = None
import keyboard
import time


i = 1
while True:
    try:
        if keyboard.is_pressed('s'):
            number = i
            t1 = time.time()
            img = ImageGrab.grab(bbox=(10,10,500,500))
            #img.show()
            img.save(f"image_{number}.png")
            t2 = time.time()
            print("The passing time",(t2-t1))
            print("The passing time",number)
            i = i+1
            #break
            time.sleep(0.1)
        elif keyboard.is_pressed('q'):
            break
        else:
            pass
    except:
        break
