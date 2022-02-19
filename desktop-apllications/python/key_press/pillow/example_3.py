from PIL import ImageGrab

filepath = 'my_image.png'

screenshot = ImageGrab.grab()
screenshot.save(filepath, 'PNG')  # Equivalent to `screenshot.save(filepath, format='PNG')`