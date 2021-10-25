#!/bin/sh
CONVERGE=1
ITER=1
rm v v1 log*

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /Assignment-2/output/task-* 

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
-mapper "'/home/pes1ug19cs217/A2/T1/mapper.py'" \
-reducer "'/home/pes1ug19cs217/A2/T1/reducer.py' '/home/pes1ug19cs217/A2/v'" \
-input /Assignment-2/Input/dataset_1percent.txt \
-output /Assignment-2/output/task-1-output

while [ "$CONVERGE" -ne 0 ]
do
	echo "############################# ITERATION $ITER #############################"
	hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
	-mapper "'/home/pes1ug19cs217/A2/T2/mapper.py' '/home/pes1ug19cs217/A2/v' '/home/pes1ug19cs217/A2/embedding_1percent.json'" \
	-reducer "'/home/pes1ug19cs217/A2/T2/reducer.py'" \
	-input /Assignment-2/output/task-1-output/part-00000 \
	-output /Assignment-2/output/task-2-output
	touch v1
	hadoop fs -cat /Assignment-2/output/task-2-output/part-00000 > "/home/pes1ug19cs217/A2/v1"
	CONVERGE=$(python3 /home/pes1ug19cs217/A2/check_conv.py $ITER>&1)
	ITER=$((ITER+1))
	hdfs dfs -rm -r /Assignment-2/output/task-2-output/
	echo $CONVERGE
done
