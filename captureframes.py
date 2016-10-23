from PIL import Image
import numpy as np
from rx import Observable
import sys
import time

def create_observable(observer):
    while True:
        time.sleep(1/5)
        raw_image = sys.stdin.read(360*640*3)

        image = np.fromstring(raw_image, dtype='uint8')
        image = image.reshape((360,640,3))

        if check_startscreen(image):
            observer.on_next('startscreen')
            continue

        p1winner = check_winner(image, 207)
        p2winner = check_winner(image, 357)
        if p1winner or p2winner:
            observer.on_next('winner is ' + ('p1' if p1winner else 'p2'))


def check_startscreen(input):
    matrix = input[10,:][380:480]
    diff = diff_to_baseline(matrix, [37, 51, 115])

    return diff < 8

def diff_to_baseline(matrix, baseline):
    mean = np.mean(matrix, axis=0)
    target = np.array(baseline)
    return np.sum(np.absolute(mean - target))

def check_winner(input, x):
    matrix = input[:,x][50:117]
    diff = diff_to_baseline(matrix, [130, 111, 0])

    return diff < 8

events = Observable.create(create_observable)

def get_winners():
    return events
