#!/usr/bin/python

import sys

count = 0

for line in sys.stdin:          # For ever line in the input from stdin
    count += 1
    if count <= 20:
        line = line.strip()         # Remove trailing characters
        print(line)
