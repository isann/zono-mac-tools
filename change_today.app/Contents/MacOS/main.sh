#!/bin/sh
year=`date '+%Y'`
month=`date '+%m'`
day=`date '+%d'`
base_dir=~/works
today_dir=$base_dir/$year/$month/$day
symlink_dir=~/Desktop

echo $today_dir
rm $symlink_dir/today
ln -s $today_dir $symlink_dir/today
echo 'success'
