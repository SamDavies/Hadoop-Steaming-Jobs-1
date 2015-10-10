#!/usr/bin/python

import sys

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()                 # remove whitespaces
    print(line)