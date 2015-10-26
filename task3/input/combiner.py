#!/usr/bin/python

import sys

word_count = 0
line_count = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    line_word_count, _ = line.split("\t", 1)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    word_count += int(line_word_count)
    line_count += 1

print("{0}\t{1}".format(word_count, line_count))
