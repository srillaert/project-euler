#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for problem in p002 p108 p800 p853; do
	echo $problem
	python3 "$SCRIPT_DIR/get_problem.py" --file "$SCRIPT_DIR/$problem.html" | diff - "$SCRIPT_DIR/../$problem.md"
done
