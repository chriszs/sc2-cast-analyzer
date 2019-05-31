#!/bin/bash

EXT=png

for file in $(find $1 -name "*."$EXT);
do
	FIRSTDIR=$(dirname $file)
	CLIP=$(basename $FIRSTDIR)
	SECONDDIR=$(dirname $FIRSTDIR)
	VIDEO=$(basename $SECONDDIR)
	FRAME=$(basename $file "."$EXT)
	DIR=$2$VIDEO"/"$CLIP"/"$FRAME"/"
	mkdir -p $DIR
	pipenv run python main.py $file $DIR
done
