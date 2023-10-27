from PIL import ImageGrab
import sys

try:
    path = sys.argv[1]
except IndexError:
    raise Exception("the save path is not received as the first command line argument") from None
image = ImageGrab.grabclipboard()
image.save(path, format=image.format)
