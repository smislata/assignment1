# -*- coding: utf-8 -*-
import argparse
from random import shuffle
# Construct parser
parser = argparse.ArgumentParser(description="Print randomly a range of integers.")

# Add arguments
parser.add_argument("-f", "--first", type=int, required=False, default=1, help="Lower Limit.", metavar="F")
parser.add_argument("-l", "--last", type=int, required=False, default=10, help="Upper Limit.", metavar="L")
args = vars(parser.parse_args())

# Arguments Validation
val1=int(args['first'])
val2=int(args['last'])+1

# Print Randomly Numbers From 1st to Last
if val1>val2:
    print("Lower Limit is bigger than Upper Limit. No number will be printed.")
else:
    list=[x for x in range(val1,val2)]
    shuffle(list)
    for x in list:
        print(x)