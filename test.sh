#!/bin/sh
if [ -z "$1" ]; then
	echo "Usage : test.sh name_of_the_project_euler_problem"
	echo "Example : test.sh p026"
else
	make $1
	./$1 | diff - $1.output
fi
