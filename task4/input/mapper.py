#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip()                 # remove whitespaces
    tokens = line.split()               # split the line into tokens

    for i in range(1, len(tokens)):     # write the results to standard output
        print("{0} {1}\t{2}".format(tokens[i-1], tokens[i], 1))
