#!/bin/sh

#!/bin/bash

# echo `pwd`
# interval=$1

# for i in `seq 1 $interval`; do
#     echo [ $$ ]  [`date +"%T"`] "Sleeping for 10 seconds"
#     sleep 10s
# done

#cd $XPCS_HADOOP_DIR
cd /home/xpcs/xpcs-0.5.0/
./multitau.sh -i $1
