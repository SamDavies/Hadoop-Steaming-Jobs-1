#!/usr/bin/python

import sys

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    pair, value = line.split("\t", 1)
    print("{0}\t{1}".format(value, pair))
