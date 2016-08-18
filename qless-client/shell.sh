#!/bin/sh

#!/bin/bash

echo `pwd`
interval=$1

for i in `seq 1 $interval`; do
    echo [ $$ ]  [`date +"%T"`] "Sleeping for 10 seconds"
    sleep 10s
done
