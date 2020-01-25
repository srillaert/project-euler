#include <stdio.h>

unsigned int sum_of_squares(unsigned int n) {
	unsigned int sum = 0;
	for(unsigned int i = 1; i <= n; i++)
		sum += i * i;

	return sum;
}

unsigned int square_of_sum(unsigned int n) {
	unsigned int sum = n * (n + 1) / 2;
	return sum * sum;
}

int main() {
	unsigned int n = 100;
	unsigned int difference = square_of_sum(n) - sum_of_squares(n);
	printf("%u\n", difference);
}
