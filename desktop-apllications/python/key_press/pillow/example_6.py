from PIL import ImageGrab

screenshot = ImageGrab.grab(all_screens=True)  # Take a screenshot that includes all screens

screenshot.save("all_screen.png", 'PNG')


 #Please note that all_screens is currently only supported in Windows