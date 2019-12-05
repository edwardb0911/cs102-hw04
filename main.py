import random
import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

# Create a new, all-white image that's the same size as the original
new_img = Image.new("RGB", (width, height), "white")

# TODO: Replace this with your own filter!
# Median pixel filter, taken from https://note.nkmk.me/en/python-opencv-pillow-image-size
#members = [0] * 9
for i in range(0, width):
    for j in range(0, height):
        #members[1] = img.getpixel((i - 1, j))
        #members[2] = img.getpixel((i - 1, j + 1))
        #members[3] = img.getpixel((i, j - 1))
        #members[4] = img.getpixel((i, j))
        #members[5] = img.getpixel((i, j + 1))
        #members[6] = img.getpixel((i + 1, j - 1))
        #members[7] = img.getpixel((i + 1, j))
        #members[8] = img.getpixel((i + 1, j + 1))
        new_img.putpixel((i, j), (img.getpixel(width - i, height - j)))

new_img.save(output_path)
