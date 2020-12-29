#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

bool is_prime(uint_fast32_t n) {
	uint_fast32_t till = sqrt(n);
	for(uint_fast32_t i = 3; i <= till; i+=2)
		if(n%i == 0)
			return false;
	return true;
}


int main() {
	uint_fast32_t number = 1;
	for(uint_fast16_t count = 1; count < 10001;) {
		number += 2;
		if(is_prime(number))
			count++;
	}
	printf("%lu\n", number);
}
