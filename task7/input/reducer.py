#!/usr/bin/python

import sys

prev_col = ""
col = ""

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    key, value = line.split("\t", 1)
    col, row = line.split(",", 1)
    value = int(value)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_col != col:
        if prev_col:  # write result to stdout
            print("")
        prev_col = col
        sys.stdout.write("{0}\t{1}".format(col, value))
    else:
        sys.stdout.write("\t{0}".format(value))


if prev_col == col:  # Don't forget the last key/value pair
    print("")
