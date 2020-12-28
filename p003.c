#include <math.h>
#include <stdint.h>
#include <stdio.h>

int main(void) {
	uint_fast64_t number = 600851475143; // 13195
	uint_fast64_t till = sqrt(number);
	uint_fast64_t n = 2;

	while(n <= till) {
		while(number % n == 0) {
			number = number / n;
			till = sqrt(number);
		}
		n += 1;
	}
	printf("%lu\n", number);
}
