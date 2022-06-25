#include "p719_lib.c"
#include<stdio.h>
#include<stdint.h>

// Takes too much time, more than a minute on a Thinkpad X1 Gen3 : 1m11,018s
int main() {
	int64_t result = sum_S_numbers(1000000);
	printf("%ld\n", result);
}
