import detect
import time

import mic

import argparse
import threading

'''
####################
    Parse Inputs
####################
'''
parser = argparse.ArgumentParser(
                    prog = 'Baby Monitor',
                    description = '')
parser.add_argument('--vis', dest='visualize',
                    action='store_true')
parser.add_argument('--fig', dest='figure',
                    action='store_true')
args = parser.parse_args()


'''
####################
     Main Loop
####################
'''

if __name__ == "__main__":
    detect.init()
    # detect.start(visualize=args.visualize)
    # mic.record(visualize=args.visualize)

    stop_event = threading.Event()
    event_dict = {'stop': stop_event}
    thread_detect = threading.Thread(target=detect.start, args=(event_dict, args,))
    thread_mic = threading.Thread(target=mic.record, args=(event_dict, args,))
    thread_detect.start()
    thread_mic.start()

    while True:
        try:
            pass
        except KeyboardInterrupt:
            stop_event.set()
            thread_detect.join()
            thread_mic.join()
            break
