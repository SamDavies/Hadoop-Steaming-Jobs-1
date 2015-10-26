#!/bin/sh

echo "hdfs dfs -rm -r /user/\$USER/data/output/ ;
      hdfs dfs -rm -r /user/\$USER/data/input/ ;
      hdfs dfs -copyFromLocal /afs/inf.ed.ac.uk/user/s12/s1220039/Documents/EXC/Assignment1/task5/output/ /user/\$USER/data/ &&
      hdfs dfs -mv /user/\$USER/data/output /user/\$USER/data/input &&
      hdfs dfs -rm /user/\$USER/data/input/_SUCCESS &&
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
 -D mapred.text.key.comparator.options=-nr \
 -D mapreduce.job.reduces=1 \
 -input /user/\$USER/data/input/ \
 -output /user/\$USER/data/output \
 -mapper mapper.py \
 -file Documents/EXC/Assignment1/task6/input/mapper.py \
 -combiner combiner.py \
 -file Documents/EXC/Assignment1/task6/input/combiner.py \
 -reducer reducer.py \
 -file Documents/EXC/Assignment1/task6/input/reducer.py \
 -jobconf mapred.job.name=\"Sam's top 20 pairs\" ;"