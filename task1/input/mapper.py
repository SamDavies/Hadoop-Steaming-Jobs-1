#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip()         # Remove trailing characters
    if line:
        print(line.lower())
