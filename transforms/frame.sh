#!/bin/bash

EXT=mp4

for file in $(find $1 -name "*."$EXT);
do
	DIR=$2$(basename $(dirname $file))"/"$(basename $file "."$EXT)"/"
	if [ ! -d $DIR ]; then
		mkdir -p $DIR
		ffmpeg -i $file -vf fps=1 $DIR%d.png
	fi
done
