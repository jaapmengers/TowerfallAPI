from __future__ import print_function
import time
import captureinputs as ci
import captureframes as cf
import predict
from rx import Observable

winners = cf.get_winners() \
    .distinct_until_changed() \

events = ci.get_event_summary() \
    .map(predict.predict_player) \
    .map(predict.player_for_score) \

winners.merge(events) \
    .subscribe(lambda e: print(e))

while 1:
    time.sleep(0.1)
