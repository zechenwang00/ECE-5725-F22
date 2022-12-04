import detect

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
while True:
    detect.init()
    if args.visualize:
        detect.start(True)
    else:
        detect.start(False)