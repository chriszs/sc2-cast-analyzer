#!/bin/bash

#for file in $(find $1 -name "*.txt");
#do

ID=zoIeC19F3q8
EXT=mp4

if [ ! -f $1"/"$ID"."$EXT ]; then
	pipenv run youtube-dl -f "bestvideo[ext="$EXT"]" -o $1"%(id)s.%(ext)s" --write-info-json "https://youtu.be/"$ID
fi
#done
