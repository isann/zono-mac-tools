#!/bin/bash
# echo 'enter year and maonth YYYYMM'
# read YYYYMM
BASE_DIR=~/works
if [ ! -f /usr/bin/php ]; then
    mkdir -p $BASE_DIR
fi
YYYYMM=`date '+%Y%m'`
YYYY=`echo ${YYYYMM} | cut -c-4`
MM=`echo ${YYYYMM} | cut -c5-6`
mkdir -p $BASE_DIR/${YYYY}
mkdir -p $BASE_DIR/${YYYY}/${MM}
for i in {1..31};
do
    if [[ ${#i} == 1 ]];then
  mkdir -p $BASE_DIR/${YYYY}/${MM}/0${i}
    else
  mkdir -p $BASE_DIR/${YYYY}/${MM}/${i}
    fi
done
echo 'success'
