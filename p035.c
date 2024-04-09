#include<stdbool.h>
#include<stdio.h>

#define EXCLUSIVE_UPPER_BOUND 1000000
#define SQRT_EXCLUSIVE_UPPER_BOUND 1000

bool is_prime[EXCLUSIVE_UPPER_BOUND];

void initialize_sieve_of_eratosthenes() {
	for(int i=2; i<EXCLUSIVE_UPPER_BOUND; i++) 
		is_prime[i] = true;
	for(int i=2; i<SQRT_EXCLUSIVE_UPPER_BOUND; i++)
		if(is_prime[i] == true)
			for(int multiple=i*i; multiple<EXCLUSIVE_UPPER_BOUND; multiple+=i)
				is_prime[multiple] = false;
}

int main() {
	initialize_sieve_of_eratosthenes();

	int count = 4; // 2, 3, 5 and 7 are circular primes but we start the loop later at 11
	for(int power_of_10 = 10; power_of_10 < EXCLUSIVE_UPPER_BOUND; power_of_10 *= 10) {
		for(int n = power_of_10 + 1; n < power_of_10 * 10; n++) {
			if(is_prime[n] == true) {
				int rotate = n;
				do {
					rotate = (rotate % 10) * power_of_10 + rotate / 10;
				} while(rotate != n && is_prime[rotate]);
				if(rotate == n)
					count++;
			}
		}
	}

	printf("%d\n", count);
}
