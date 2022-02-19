from PIL import ImageGrab

file = open('my_file.png', 'wb')


screenshot = ImageGrab.grab()
screenshot.save(file, 'PNG')  # Save the image to the file object as a PNG

file.close()  # Make sure to close the file when you're done