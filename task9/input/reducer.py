#!/usr/bin/python

import sys

prev_student = ""
student = ""
current_name = ""
current_count = 0
current_total = 0
min_name = ""
min_average = 100

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t", 1)
    student, table = key.split(",", 1)
    
    if prev_student != student:
        # we are on a new student so check if the previous student is the new min
        if prev_student:
            # only allow a student with more than 4 grades
            if current_count > 4:
                # check if he is the new min
                current_average = current_total/float(current_count)
                if current_average < min_average:
                    min_name = current_name
                    min_average = current_average

        # set up the new student
        prev_student = student
        current_count = 0
        current_total = 0

    # save the students name
    if table == "0":
        current_name = value
    else:
        # add to his average
        subject, grade = value.split()
        current_count += 1
        current_total += int(grade)


# remember to check the last record
if prev_student == student:
    # only allow a student with more than 4 grades
    if current_count > 4:
        # check if he is the new min
        current_average = current_total/float(current_count)
        if current_average < min_average:
            min_name = current_name
            min_average = current_average

print("{0} {1}".format(min_average, min_name))
