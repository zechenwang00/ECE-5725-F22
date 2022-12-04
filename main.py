import detect
import mic

import argparse

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
mic.init()
detect.init()

while True:
    detect.start(visualize=args.visualize)
    mic.record(visualize=args.visualize)
