from __future__ import print_function
import capture
import predict

try:
    capture.get_event_summary() \
        .map(predict.predict_player) \
        .map(predict.player_for_score) \
        .subscribe(lambda e: print(e))
except Exception as ex:
    print("Test")
    print(ex)
    raw_input()
