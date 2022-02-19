from PIL import Image, ImageGrab
import keyboard

while True:
    try:
        if keyboard.is_pressed('s'):
            img = ImageGrab.grab(bbox=(10,10,500,500))
            img.show()
            #img.save("image.png")
           
            #break
        elif keyboard.is_pressed('q'):
            break
        else:
            pass
    except:
        break
