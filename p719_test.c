#include "p719_lib.c"
#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>

void assert_bool(bool expected, bool actual, char* message) {
	if(expected != actual) {
		printf("expected %d but actual %d for %s\n", expected, actual, message);
	}
}

void assert_int64_t(int64_t expected, int64_t actual, char* message) {
	if(expected != actual) {
		printf("expected %ld but actual %ld for %s\n", expected, actual, message);
	}
}

void assert_sum_decimal_split(int64_t to_split, int64_t sum, bool expected) {
	bool actual = sum_decimal_split_equals(to_split, sum);
	char message[100];
	sprintf(message, "sum_decimal_split_equals_equals(%ld, %ld)", to_split, sum);
	assert_bool(expected, actual, message);
}

int main() {
	assert_sum_decimal_split(16, 4, false);
	assert_sum_decimal_split(81, 9, true); // 81 is the first S-number
	assert_sum_decimal_split(6724, 82, true); // first example
	
	int64_t actual = sum_S_numbers(100);
	assert_int64_t(41333, actual, "example T(10^4) = 41333");
}
