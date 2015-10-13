#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip()                 # remove whitespaces
    tokens = line.split()               # split the line into tokens

    combiner = dict()

    for i in range(1, len(tokens)):     # write the results to standard output
        key = "{0} {1}".format(tokens[i-1], tokens[i])
        if combiner.get(key):
            combiner[key] += 1
        else:
            combiner[key] = 1

    for key, value in combiner.items():     # write the results to standard output
        print("{0}\t{1}".format(key, value))
