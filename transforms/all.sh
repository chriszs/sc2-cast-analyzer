#!/bin/bash

transforms=( 'download' 'split' 'extract' ) # 'check' 'download' 'split' 'extract' 'ocr'

prior=''

for transform in "${transforms[@]}"
do
	echo $transform
	mkdir -p ./data/$transform
	if [ $prior ];
	then
		./transforms/$transform.sh ./data/$prior/ ./data/$transform/
	else
		./transforms/$transform.sh ./data/$transform/
	fi
	
	prior=$transform
done
