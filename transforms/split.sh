#!/bin/bash

EXT=mp4

for file in $(find $1 -name "*."$EXT);
do
	DIR=$2$(basename $file "."$EXT)"/"
	if [ ! -d $DIR ]; then
		mkdir -p $DIR
		echo $DIR
		ffmpeg -i $file -acodec copy -f segment -segment_time 10 -vcodec copy -reset_timestamps 1 -map 0 $DIR%d"."$EXT
	fi
done
