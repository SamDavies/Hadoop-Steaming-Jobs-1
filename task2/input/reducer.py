#!/usr/bin/python

import sys

prev_line = ""
this_line = ""

for line in sys.stdin:          # For ever line in the input from stdin
    this_line = line.strip()         # Remove trailing characters
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_line != this_line:
        print(prev_line)
        prev_line = this_line

if prev_line == this_line:  # Don't forget the last line
    print(prev_line)
