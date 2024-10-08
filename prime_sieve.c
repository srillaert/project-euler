#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include "prime_sieve.h"

void prime_sieve_initialize(SIEVE_WORD_TYPE* sieve, uint_fast32_t size_sieve, uint_fast32_t exclusive_till) {
	for(uint_fast32_t i = 0; i < size_sieve; i++)
		sieve[i] = SIEVE_WORD_MAX; // By default, set all the numbers to be primes

	// Perform the sieve
	uint_fast32_t till = floor(sqrt(exclusive_till));
	for(uint_fast32_t i = 2; i <= till; i++) {
		if(prime_sieve_is_prime(sieve, i))  // If the number is a prime, check off all its multiples
			for(uint_fast32_t j = i*i; j < exclusive_till; j += i)
				sieve[j / SIEVE_WORD_BIT_LEN] &= ~(1 << (j % SIEVE_WORD_BIT_LEN));
	}
}

bool prime_sieve_is_prime(SIEVE_WORD_TYPE* sieve, uint_fast32_t n) {
	return sieve[n / SIEVE_WORD_BIT_LEN] & (1 << (n % SIEVE_WORD_BIT_LEN));
}