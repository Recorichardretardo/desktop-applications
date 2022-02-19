import keyboard


while True:
    keyboard.wait("s")
    if keyboard.press("shift+s"):
        print("came here")
   