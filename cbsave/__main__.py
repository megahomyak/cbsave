from PIL import ImageGrab
from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument("path")
parser.add_argument("-e", "--guess-extension", action="store_true")

args = parser.parse_args()

image = ImageGrab.grabclipboard()
path = args.path
if args.guess_extension:
    path, _old_ext = os.path.splitext(args.path)
    path = path + "." + image.format.lower()
image.save(path, format=image.format)
