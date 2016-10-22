from PIL import Image
import numpy as np
import imageprocessing as ip
import sys

while True:
    raw_image = sys.stdin.read(1280*720*3)

    # transform the byte read into a numpy array
    image = np.fromstring(raw_image, dtype='uint8')
    image = image.reshape((720,1280,3))

    img = Image.fromarray(image, 'RGB')
    img.show()

    # ip.test(image)
