#!/usr/bin/python

import sys

prev_phrase = ""
value_total = 0
phrase = ""

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    phrase, value = line.split("\t", 1)
    value = int(value)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_phrase == phrase:
        value_total += value
    else:
        if prev_phrase:  # write result to stdout
            print("{0}\t{1}".format(prev_phrase, value_total))
            
        value_total = value
        prev_phrase = phrase

if prev_phrase == phrase:  # Don't forget the last key/value pair
    print("{0}\t{1}".format(prev_phrase, value_total))
