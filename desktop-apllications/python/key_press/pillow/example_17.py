from PIL import Image, ImageGrab
import keyboard
import time



while True:
    try:
        time.sleep(1)
        if keyboard.is_pressed('s'):
            t1 = time.time()
            print("The passing time",t1)
        elif keyboard.is_pressed('q'):
            break
        else:
            pass
    except:
        break
