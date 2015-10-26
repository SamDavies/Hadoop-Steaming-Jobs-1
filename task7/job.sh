#!/bin/sh

echo "hdfs dfs -rm -r /user/\$USER/data/output/ ;
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D mapreduce.map.output.key.field.separator=, \
 -D stream.map.output.field.separator=, \
 -D stream.num.map.output.key.fields=2 \
 -D num.key.fields.for.partition=1 \
 -D mapred.text.key.comparator.options='-k1,1n -k2,2n' \
 -D mapreduce.partition.keypartitioner.options=-k1,1 \
 -D mapreduce.job.reduces=9 \
 -input /data/assignments/ex1/matrixLarge.txt \
 -output /user/\$USER/data/output \
 -mapper mapper.py \
 -reducer reducer.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
 -file Documents/EXC/Assignment1/task7/input/mapper.py \
 -file Documents/EXC/Assignment1/task7/input/reducer.py \
 -jobconf mapred.job.name=\"Sam's matrix transpose\" ;
 hdfs dfs -cat /user/\$USER/data/output/* | sort -n | awk '{\$1=\"\";print substr(\$0,2);}' | hdfs dfs -put - /user/\$USER/data/output/result.txt;"