from PIL import Image
import numpy as np
import imageprocessing as ip
from rx import Observable
import sys
import time

def create_observable(observer):
    while True:
        raw_image = sys.stdin.read(360*640*3)

        image = np.fromstring(raw_image, dtype='uint8')
        image = image.reshape((360,640,3))

        p1winner = test(image, 207)
        p2winner = test(image, 357)
        if p1winner or p2winner:
            observer.on_next('winner is ' + ('p1' if p1winner else 'p2'))
        else:
            print 'No winner'

        time.sleep(1)

def test(input, x):
    pixels = range(50, 117)

    matrix = input[:,x][50:117]

    mean = np.mean(matrix, axis=0)
    target = np.array([130, 111, 0])
    diff = np.sum(np.absolute(mean - target))

    return diff < 8

events = Observable.create(create_observable)

def get_winners():
    return events
