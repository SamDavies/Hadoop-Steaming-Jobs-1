#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    row, numbers = line.split("\t", 1)

    numbers_array = numbers.split()

    for col, number in enumerate(numbers_array):
        print("{0},{1},{2}".format(col, row, number))
