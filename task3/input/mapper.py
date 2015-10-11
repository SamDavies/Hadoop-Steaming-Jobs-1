#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip()                 # remove whitespaces
    tokens = line.split()               # split the line into tokens

    print("{0}\t{1}".format(len(tokens), 1))
