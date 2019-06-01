#!/bin/bash

#for file in $(find $1 -name "*.txt");
#do

ID=zoIeC19F3q8
EXT=mp4

if [ ! -f $1"/"$ID"."$EXT ]; then
	# streamlink --stdout https://www.youtube.com/watch?v=sHT1bYAlCIk best | ffmpeg -i pipe:0 -c copy -f segment -segment_time 10 -reset_timestamps 1 -map 0 ./%d".mp4"
	pipenv run youtube-dl -f "bestvideo[ext="$EXT"]" -o $1"%(id)s.%(ext)s" --write-info-json "https://youtu.be/"$ID
fi
#done
