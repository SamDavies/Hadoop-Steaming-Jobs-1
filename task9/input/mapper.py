#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    elements = line.split()

    if len(elements) == 3:
        print("{0},{1}\t{2}".format(elements[1], 0, elements[2]))

    if len(elements) == 4:
        print("{0},{1}\t{2} {3}".format(elements[2], 1, elements[1], elements[3]))
