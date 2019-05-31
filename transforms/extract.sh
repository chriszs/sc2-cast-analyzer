#!/bin/bash

for file in $(find $1 -name "*.mp4");
do
	pipenv run python main.py $file $2/$(basename $file .mp4)
done
