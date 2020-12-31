#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

#define MAX 2000000
#define SIZE_SIEVE_ARRAY ((MAX - 1) / 8) + 1

int main() {
	// Initialize the sieve of Eratosthenes
	uint8_t sieve[SIZE_SIEVE_ARRAY];
	for(uint_fast32_t i = 0; i < SIZE_SIEVE_ARRAY; i++)
		sieve[i] = UINT8_MAX; // By default, set all the numbers to be primes

	// Perform the sieve
	uint_fast32_t till = floor(sqrt(MAX));
	for(uint_fast32_t i = 2; i <= till; i++) {
		if(sieve[i / 8] & (1 << (i % 8)))  // If the number is a prime, check off all its multiples
			for(uint_fast32_t j = 2*i; j < MAX; j += i)
				sieve[j / 8] &= ~(1 << (j % 8));
	}

	// Calculate the sum of the primes
	uint_fast64_t sum = 0;
	for(uint_fast32_t i = 2; i < MAX; i++)
		if(sieve[i / 8] & (1 << (i % 8)))
			sum += i;

	printf("%lu\n", sum);
}
