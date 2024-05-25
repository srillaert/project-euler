#include <stdint.h>
#include <stdio.h>
#include "prime_sieve.h"

#define MAX 2000000
#define SIZE_SIEVE_ARRAY ((MAX - 1) / 8) + 1

int main() {
	// Initialize the sieve of Eratosthenes
	uint8_t sieve[SIZE_SIEVE_ARRAY];
	prime_sieve_initialize(sieve, SIZE_SIEVE_ARRAY, MAX);

	// Calculate the sum of the primes
	uint_fast64_t sum = 0;
	for(uint_fast32_t i = 2; i < MAX; i++)
		if(prime_sieve_is_prime(sieve, i))
			sum += i;

	printf("%lu\n", sum);
}