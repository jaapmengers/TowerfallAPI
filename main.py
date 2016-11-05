from __future__ import print_function
import time
import captureinputs as ci
import captureframes as cf
import predict
from rx import Observable

# cf.record('frames')

ci.record('inputs')

# game_events = cf.game_events() \
#     .distinct_until_changed() \
#
# events = ci.get_event_summary() \
#     .map(predict.predict_player) \
#     .map(predict.player_for_score) \
#
# starts = game_events.filter(lambda e: e[0] == 'startscreen')
# winners = game_events.filter(lambda e: e[0] == 'winner')
#
# game_events.merge(events) \
#     .subscribe(lambda e: print(e))

while 1:
    time.sleep(0.1)
