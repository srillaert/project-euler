#include <math.h>
#include <stdio.h>

#define MAX 2000000

int main() {
	// Initialize the sieve of Eratosthenes
	char sieve[MAX - 2];
	for(int i = 0; i < (MAX - 2); i++)
		sieve[i] = 1; // By default, set all the numbers to be primes

	// Perform the sieve
	unsigned int till = floor(sqrt(MAX));
	for(int i = 2; i <= till; i++) {
		if(sieve[i-2])  // If the number is a prime, check off all its multiples
			for(int j = 2*i; j < MAX; j += i)
				sieve[j-2] = 0;
	}

	// Calculate the sum of the primes
	unsigned long long sum = 0;
	for(int i = 0; i < (MAX - 2); i++)
		if(sieve[i])
			sum += i + 2;

	printf("%llu\n", sum);
}
