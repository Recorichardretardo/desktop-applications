from pynput import keyboard

def function_1():
    print('Function 1 activated')

def function_2():
    quit()

with keyboard.GlobalHotKeys({
        '<alt>+<ctrl>+r': function_1,
        '<alt>+<ctrl>+t': function_1,
        '<alt>+<ctrl>+y': function_2}) as h:
    h.join()