from pynput import keyboard
from pynput.keyboard import Controller, Listener, Key

c = Controller()

typed = []
tString = ""
message = "Kind Regards,\n\nJohn Smith, Sales Manager"

def press_callback(key):
    if hasattr(key,'char'):
        for letter in "abcdefghijklmnopqrstuvwxyz.":
            if key.char == letter:
                typed.append(letter)
                if len(typed)>4:
                    typed.pop(0)
                tString = ','.join(typed).replace(',','')
                print(tString)
                if tString == "k...":
                    for _ in range(4):
                        c.press(Key.backspace)
                        c.release(Key.backspace) 
                    c.type(message)

l = Listener(on_press=press_callback)

l.start()
l.join()