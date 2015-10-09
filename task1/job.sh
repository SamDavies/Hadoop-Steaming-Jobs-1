#!/bin/sh

echo "hdfs dfs -rm -r /user/\$USER/data/output/; hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -input /user/\$USER/data/input \
 -output /user/\$USER/data/output \
 -mapper mapper.py \
 -file Documents/EXC/Assignment1/task1/input/mapper.py \
 -reducer reducer.py \
 -file Documents/EXC/Assignment1/task1/input/reducer.py \
 -jobconf mapred.job.name=\"Sam's Word counter\""