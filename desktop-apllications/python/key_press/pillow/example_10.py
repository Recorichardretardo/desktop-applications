from PIL import Image, ImageGrab
Image.MAX_IMAGE_PIXELS = None
import keyboard
import time



while True:
    try:
        if keyboard.is_pressed('s'):
            t1 = time.time()
            img = ImageGrab.grab(bbox=(10,10,500,500))
            img.show()
            #img.save("image.png")
            t2 = time.time()
            print("The passing time",(t2-t1))
           
            #break
        elif keyboard.is_pressed('q'):
            break
        else:
            pass
    except:
        break
