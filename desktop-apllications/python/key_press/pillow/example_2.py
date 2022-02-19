from PIL import Image, ImageGrab
import keyboard

while True:
    try:
        if keyboard.is_pressed('q'):
            img = ImageGrab.grab()
            # img.show()
            img.save("image.png")
           
            break
        else:
            pass
    except:
        break
