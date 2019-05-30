#!/bin/bash

for file in $(find $1 -name "*.mp4");
do
	ffmpeg -i $file -acodec copy -f segment -segment_time 10 -vcodec copy -reset_timestamps 1 -map 0 $2%d.mp4
done
