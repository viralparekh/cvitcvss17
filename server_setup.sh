#!/bin/bash

if [ $# -ne 1 ] ; then
    echo "./server_setup.sh <daynum>"
    exit 1
fi

day=$1
numusers=14
startport=8000
interval=10
numgpus=4

DATAPATH="/users/summerschool/cvdata"
CODEPATH="/users/summerschool/cvitcvss17"
WORKPATH="/tmp/summerschool/user"

for i in `seq 1 $numusers` ; do
    destdir="$WORKPATH${i}"
    mkdir -p $destdir
    cp -av $CODEPATH/lab${day} $destdir
    cd $destdir
    #echo `pwd`
    #echo $(($startport+($i-1)*$interval))
     echo $(($i%$numgpus))
     CUDA_VISIBLE_DEVICES=$(($i%$numgpus)) jupyter notebook --no-browser --ip="0.0.0.0" --port=$(($startport+($i-1)*$interval)) &
    cd
done
