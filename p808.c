#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include "prime_sieve.h"

#define MAX 100000000
#define SIZE_SIEVE_ARRAY ((MAX - 1) / 8) + 1

uint8_t sieve[SIZE_SIEVE_ARRAY];

uint_fast32_t reverse(uint_fast64_t n) {
	uint_fast64_t result = 0;
	while (n > 0) {
		result = result * 10 + n % 10;
		n /= 10;
	}
	return result;
}

bool is_reversable_prime_square(uint64_t n) {
	uint_fast64_t rev = reverse(n);
	if (rev == n) return false;
	uint_fast32_t sqrt_rev = (uint_fast32_t)sqrt((double)rev);
	return (sqrt_rev * sqrt_rev == rev) && prime_sieve_is_prime(sieve, sqrt_rev);
}

int main() {
	prime_sieve_initialize(sieve, SIZE_SIEVE_ARRAY, MAX);

	uint_fast64_t sum = 0;
	uint_least8_t count = 0;
	for(uint_fast32_t i = 2; i < MAX; i++)
		if(prime_sieve_is_prime(sieve, i)) {
			uint_fast64_t square = (uint_fast64_t)i * (uint_fast64_t)i;
			if (is_reversable_prime_square(square)) {
				sum += square;
				count += 1;
				if (count == 50) break;
			}
		}
	printf("%lu\n", sum);
}