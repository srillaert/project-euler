#include <stdint.h>
#include <stdio.h>
#include "prime_sieve.h"

#define SIZE_SIEVE_ARRAY 2
#define MAX (SIZE_SIEVE_ARRAY * SIEVE_WORD_BIT_LEN) - 1

SIEVE_WORD_TYPE sieve[SIZE_SIEVE_ARRAY];

int passed = 0;
int failed = 0;

void assert_is_composite(uint_fast32_t n) {
	if(prime_sieve_is_prime(sieve, n)) {
		failed++;
		printf("expected %lu to be a composite number\n", n);
	} else {
		passed++;
	}
}

void assert_is_prime(uint_fast32_t n) {
	if(!prime_sieve_is_prime(sieve, n)) {
		failed++;
		printf("expected %lu to be a prime\n", n);
	} else {
		passed;
	}
}

int main() {
	prime_sieve_initialize(sieve, SIZE_SIEVE_ARRAY, MAX);

	assert_is_prime(2);
	assert_is_prime(3);
	assert_is_composite(4);
	assert_is_prime(5);
	assert_is_composite(9);

	printf("test result: %d passed; %d failed;\n", passed, failed);
}
