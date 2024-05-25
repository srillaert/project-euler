#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include "prime_sieve.h"

void prime_sieve_initialize(uint8_t* sieve, uint_fast32_t size_sieve, uint_fast32_t exclusive_till) {
	for(uint_fast32_t i = 0; i < size_sieve; i++)
		sieve[i] = UINT8_MAX; // By default, set all the numbers to be primes

	// Perform the sieve
	uint_fast32_t till = floor(sqrt(exclusive_till));
	for(uint_fast32_t i = 2; i <= till; i++) {
		if(sieve[i / 8] & (1 << (i % 8)))  // If the number is a prime, check off all its multiples
			for(uint_fast32_t j = i*i; j < exclusive_till; j += i)
				sieve[j / 8] &= ~(1 << (j % 8));
	}
}

bool prime_sieve_is_prime(uint8_t* sieve, uint_fast32_t n) {
	return sieve[n / 8] & (1 << (n % 8));
}