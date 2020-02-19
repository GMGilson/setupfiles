#!/bin/bash

FILE='./CMakeLists.txt'
if test -f "$FILE"; then
	cmake -H. -B bin && make -j4 -C bin

else
	echo "$FILE not found Zz.."

fi

