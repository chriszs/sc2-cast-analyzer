#!/bin/bash

for file in $(find $1 -name "*.mp4");
do
	mkdir -p $2$(basename $file .mp4)/
	# ffmpeg -i $file -acodec copy -f segment -segment_time 10 -vcodec copy -reset_timestamps 1 -map 0 $2$(basename $file .mp4)/%d.mp4
	ffmpeg -i $file -vf fps=1 $2$(basename $file .mp4)/%d.png
done
