#!/bin/sh

echo "hdfs dfs -rm -r /user/\$USER/data/output/ ;
      hdfs dfs -rm -r /user/\$USER/data/input/ ;
      hdfs dfs -mkdir /user/\$USER/data/input &&
      hdfs dfs -copyFromLocal /afs/inf.ed.ac.uk/user/s12/s1220039/Documents/EXC/Assignment1/task1/output/part-00000 /user/\$USER/data/input/lower-case &&
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -input /user/\$USER/data/input/lower-case \
 -output /user/\$USER/data/output \
 -mapper mapper.py \
 -file Documents/EXC/Assignment1/task2/input/mapper.py \
 -reducer reducer.py \
 -file Documents/EXC/Assignment1/task2/input/reducer.py \
 -jobconf mapred.job.name=\"Sam's Deduplicater\""