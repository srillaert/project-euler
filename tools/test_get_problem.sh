#!/bin/bash
cd "$(dirname "${BASH_SOURCE[0]}")"

for problem in p002 p108 p800 p853; do
	echo $problem
	python3 get_problem.py --file $problem.html | diff - ../$problem.md
done
