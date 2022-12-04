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
args = parser.parse_args()


'''
####################
     Main Loop
####################
'''

detect.init()
# detect.start(visualize=args.visualize)
# mic.record(visualize=args.visualize)


thread_test = threading.Thread(target=detect.start(), args=(args.visualize,))
thread_mic = threading.Thread(target=mic.record, args=(args.visualize,))
thread_test.start()
thread_mic.start()
