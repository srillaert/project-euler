#!/bin/bash
cd "$(dirname "${BASH_SOURCE[0]}")"

problem_number="$1"
if [ -z "$problem_number" ]; then
	echo "Error: Please provide a three digit problem number as an argument."
	echo "Example: $0 001"
	exit 1
fi

wget -O get_problem_integration_tests/p${problem_number}.html  https://projecteuler.net/problem=${problem_number}
