#include <math.h>
#include <stdint.h>
#include <stdio.h>

uint_fast64_t get_largest_prime_factor(uint_fast64_t number) {
	uint_fast64_t till = sqrt(number);
	uint_fast64_t n = 2;
	while(n <= till) {
		while(number % n == 0) {
			number = number / n;
			till = sqrt(number);
		}
		n += 1;
	}
	return number;	
}

int main(void) {
	uint_fast64_t number = 600851475143;
	uint_fast64_t solution = get_largest_prime_factor(number);
	printf("%lu\n", solution);
}
