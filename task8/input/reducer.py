#!/usr/bin/python

import sys

prev_student = ""
student = ""
name = ""

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t", 1)
    student, table = key.split(",", 1)
    
    if prev_student != student:
        if prev_student:
            print("")
        prev_student = student
        sys.stdout.write("{0} -->".format(value))
    else:
        subject, grade = value.split()
        sys.stdout.write(" ({0}, {1})".format(subject, grade))

if prev_student == student:
    print("")
