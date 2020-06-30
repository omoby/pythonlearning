#!/bin/bash
task_id=$1
instance_id=$2
data_size=$3
process_num=$4
tm=$(date +%Y%m%d)
#echo task_id: $task_id
detail_log_name='detail'_${task_id}_${instance_id}_$tm
#convenio_log_name='convenio'_${task_id}_${instance_id}_$tm
#echo log_name: $log_name
#echo process_num: $process_num
# shellcheck disable=SC2109
if [ ! $data_size ]; then
   data_size=9
elif [ $data_size -le 0 ];then
   data_size=9
elif [ $data_size -le 12 ]; then
   data_size=$data_size
else
   data_size=9
fi

if [ ! $process_num  ]; then
  for ((i=1; i <= 5; i++))
  do
#  nohup python ./peru-py/convenio_start.py $task_id $instance_id  $data_size > ./log/${convenio_log_name}.log 2>&1 &
  nohup python ./peru-py/detail_start.py $task_id $instance_id  $data_size > ./log/${detail_log_name}.log 2>&1 &
  done
elif [ $process_num -le 10 ]; then
  for((i=1; i<=$process_num; i++))
     do
#      nohup python ./peru-py/convenio_start.py $task_id $instance_id  $data_size > ./log/${convenio_log_name}.log 2>&1 &
      nohup python ./peru-py/detail_start.py $task_id $instance_id  $data_size > ./log/${detail_log_name}.log 2>&1 &
     done
else
  for((i=1; i<=10; i++))
     do
#      nohup python ./peru-py/convenio_start.py $task_id $instance_id  $data_size > ./log/${convenio_log_name}.log 2>&1 &
      nohup python ./peru-py/detail_start.py $task_id $instance_id  $data_size > ./log/${detail_log_name}.log 2>&1 &
     done
fi
