from __future__ import print_function
import hid
import time
from rx import Observable
from itertools import groupby
from rx.core import AnonymousObservable
from rx.concurrency import current_thread_scheduler

h = hid.device()
h.open(1356, 1476)

def create_observable(observer):
    while True:
        result = readInputs()
        observer.on_next(result)
        time.sleep(1/250)

def getbit(v, i):
    return (v >> i) & 1

def readInputs():
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

events = Observable.create(create_observable)


# with open('data/jaap5.txt') as f:
#     lines = [line.rstrip('\n') for line in f]
#
# events = Observable.from_(lines)
#
def average(items):
    if len(items) < 1:
        return 0.0

    return sum(items, 0.0) / len(items)

def get_button_summary(events):
    ones = []

    for key, group in groupby(events, lambda x: x):
        if key == 1:
            ones.append(list(group))

    return (len(ones), average(map(lambda o: len(o), ones)))

def summarize_all_buttons(events):
    sqrSummary = get_button_summary(map(lambda e: e[0], events))
    xSummary = get_button_summary(map(lambda e: e[1], events))
    oSummary = get_button_summary(map(lambda e: e[2], events))
    triSummary = get_button_summary(map(lambda e: e[3], events))
    l1Summary = get_button_summary(map(lambda e: e[4], events))
    r1Summary = get_button_summary(map(lambda e: e[5], events))
    l2Summary = get_button_summary(map(lambda e: e[6], events))
    r2Summary = get_button_summary(map(lambda e: e[7], events))
    return [
    sqrSummary[0],
    sqrSummary[1],
    xSummary[0],
    xSummary[1],
    oSummary[0],
    oSummary[1],
    triSummary[0],
    triSummary[1],
    l1Summary[0],
    l1Summary[1],
    r1Summary[0],
    r1Summary[1],
    l2Summary[0],
    l2Summary[1],
    r2Summary[0],
    r2Summary[1]
    ]

events.buffer_with_count(2500) \
    .map(summarize_all_buttons) \
    .subscribe(lambda e: print(e))

events.map(lambda e: e.split(',')).map(lambda e: int(e)).subscribe(lambda e: print(e))
