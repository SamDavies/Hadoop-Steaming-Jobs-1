#!/bin/sh

TASK="$1"

DIR="${PWD}"

scp -rp $DIR/$TASK/input s1220039@student.ssh.inf.ed.ac.uk:/afs/inf.ed.ac.uk/user/s12/s1220039/Documents/EXC/Assignment1/$TASK/

# remove the existing output directory
ssh -t -t s1220039@student.ssh.inf.ed.ac.uk << EOL
    rm -r /afs/inf.ed.ac.uk/user/s12/s1220039/Documents/EXC/Assignment1/$TASK/output
    exit
EOL

echo ""
echo "JOB COMMAND"
echo "-----------"
. $TASK/job.sh
echo ""

echo "COPY RESULTS COMMAND"
echo "---------------------"
echo "hdfs dfs -copyToLocal /user/\$USER/data/output /afs/inf.ed.ac.uk/user/s12/s1220039/Documents/EXC/Assignment1/$TASK/"
echo ""

echo "LOCAL COPY RESULTS COMMAND"
echo "---------------------"
echo "scp -rp s1220039@student.ssh.inf.ed.ac.uk:/afs/inf.ed.ac.uk/user/s12/s1220039/Documents/EXC/Assignment1/$TASK/output $DIR/$TASK/"
echo ""


