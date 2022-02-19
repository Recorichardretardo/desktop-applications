from io import BytesIO
from PIL import ImageGrab

bytes_io = BytesIO()

screenshot = ImageGrab.grab()
screenshot.save(bytes_io, 'PNG')  # Save the image to bytes_io as a PNG

# Do what you want with the bytes_io object