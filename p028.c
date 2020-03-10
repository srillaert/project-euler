#include <stdio.h>

int main() {
	unsigned int sum = 1;
	unsigned int base_number = 1;
	unsigned int step = 2;
	for(int size = 3; size <= 1001; size += 2) {
		unsigned int square_sum = 4 * base_number + 10 * step;
		sum += square_sum;
		base_number += 4 * step;
		step += 2;
	}
	printf("%u\n", sum);
}
