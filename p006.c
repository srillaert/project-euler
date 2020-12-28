#include <stdint.h>
#include <stdio.h>

uint_fast32_t sum_of_squares(uint_fast8_t n) {
	uint_fast32_t sum = 0;
	for(uint_fast16_t i = 1; i <= n; i++)
		sum += i * i;

	return sum;
}

uint_fast32_t square_of_sum(uint_fast8_t n) {
	uint_fast32_t sum = n * (n + 1) / 2;
	return sum * sum;
}

int main() {
	uint_fast8_t n = 100;
	uint_fast32_t difference = square_of_sum(n) - sum_of_squares(n);
	printf("%lu\n", difference);
}
