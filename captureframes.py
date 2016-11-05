from PIL import Image
import numpy as np
from rx import Observable
import sys
import time

def run():
    raw_image = sys.stdin.read(360*640*3)

    image = np.fromstring(raw_image, dtype='uint8')
    image = image.reshape((360,640,3))

    if check_startscreen(image):
        return Observable.just(('startscreen', ))

    p1winner = check_winner(image, 207)
    p2winner = check_winner(image, 357)
    if p1winner or p2winner:
        return Observable.just(('winner', ('p1' if p1winner else 'p2')))

    return Observable.empty()


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

def grab_frame(path, i):
    filename = str(i) + '.bmp'
    print 'writing ' + filename
    raw_image = sys.stdin.read(360*640*3)
    image = np.fromstring(raw_image, dtype='uint8')
    image = image.reshape((360,640,3))

    Image.fromarray(image).save(path + '/' + filename)

def record(path):
    print 'hallo?'
    return Observable.interval(10).subscribe(lambda i: grab_frame(path, i))

# events = Observable.interval(200).flat_map(lambda _: run())

def get_game_events():
    return events
