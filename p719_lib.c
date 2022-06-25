#include<stdbool.h>
#include<stdint.h>
#include<stdio.h>

bool sum_decimal_split_equals(int64_t to_split, int64_t sum) {
	for(int64_t divider = 10;; divider *=10) {
		int64_t number = to_split % divider;
		int64_t rest = to_split / divider;
		if (rest == 0) {
			//printf("rest == 0\n");
			return sum == number;
		}
		if (sum <= number) false;
		if (sum_decimal_split_equals(rest, sum - number)) return true;
	}
}

int64_t sum_S_numbers(int64_t till_square_root) {
	int64_t sum = 0;
	for(int64_t square_root = 4; square_root <= till_square_root; square_root++) {
		int64_t square = square_root * square_root;
		if (sum_decimal_split_equals(square, square_root)) {
			sum += square;
		}
	}
	return sum;
}
