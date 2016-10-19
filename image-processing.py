from PIL import Image
import numpy as np
import os

def check_if_winner(pix ,x):
    pixels = range(50, 117)

    res = map(lambda p: list(pix[x, p]), pixels)

    matrix = np.array(res)
    mean = np.mean(matrix, axis=0)
    target = np.array([130, 111, 0])
    diff = np.sum(np.absolute(mean - target))

    return diff < 8

path = "TwitchStreamer/results3players"

for filename in os.listdir(path):
    if filename.endswith(".png"):
        img = Image.open(os.path.join(path, filename))
        pix = img.load()

        p1winner = check_if_winner(pix, 207)
        p2winner = check_if_winner(pix, 357)

        print filename + " " + str(p1winner) + " " + str(p2winner)

        continue
    else:
        continue
