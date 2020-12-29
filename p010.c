#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

#define MAX 2000000

int main() {
	// Initialize the sieve of Eratosthenes
	bool sieve[MAX - 2];
	for(size_t i = 0; i < (MAX - 2); i++)
		sieve[i] = true; // By default, set all the numbers to be primes

	// Perform the sieve
	size_t till = floor(sqrt(MAX));
	for(size_t i = 2; i <= till; i++) {
		if(sieve[i-2])  // If the number is a prime, check off all its multiples
			for(size_t j = 2*i; j < MAX; j += i)
				sieve[j-2] = false;
	}

	// Calculate the sum of the primes
	uint_fast64_t sum = 0;
	for(size_t i = 0; i < (MAX - 2); i++)
		if(sieve[i])
			sum += i + 2;

	printf("%lu\n", sum);
}
