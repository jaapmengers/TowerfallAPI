import hid
import time
import numpy as np

from rx import Observable
from itertools import groupby
from rx.core import AnonymousObservable
from rx.concurrency import current_thread_scheduler

h = hid.device()

def getbit(v, i):
    return (v >> i) & 1

def read_inputs():
    d = h.read(10)
    buttons = d[5]
    shoulders = d[6]

    sqr = getbit(buttons, 4)
    x = getbit(buttons, 5)
    o = getbit(buttons, 6)
    tri = getbit(buttons, 7)

    l1 = getbit(shoulders, 0)
    r1 = getbit(shoulders, 1)
    l2 = getbit(shoulders, 2)
    r2 = getbit(shoulders, 3)

    return [sqr, x, o, tri, l1, r1, l2, r2]

def average(items):
    if len(items) < 1:
        return 0.0

    return sum(items, 0.0) / len(items)

def get_button_summary(events):
    ones = []

    for key, group in groupby(events, lambda x: x):
        if key == 1:
            ones.append(list(group))

    res = (len(ones), average(map(lambda o: len(o), ones)))
    return res

def summarize_all_buttons(events):
    events_matrix = np.array(events)
    res = map(lambda e: get_button_summary(events_matrix[:,e]), [0,1,2,3,4,5,6,7])

    return res[6] + res[7] + res[1] + res[2]

def get_event_summary():
    h.open(1356, 1476)

    events = Observable.interval(4).map(lambda _: read_inputs())

    return events.buffer_with_count(2500) \
            .map(summarize_all_buttons)
