#include <stdio.h>

unsigned int length_collatz_sequence(unsigned int n) {
	unsigned int length = 1;
	while(n != 1) {
		length++;
		if(n % 2 == 0) 
			n = n / 2; // n is even
		else
			n = 3 * n + 1; // n is odd
	}
	return length;
}

int main(void) {
	unsigned int maximum_length = 0;
	unsigned int maximum_starting_number = 0;
	for(unsigned int starting_number = 1; starting_number < 1000000; starting_number++) {
		unsigned int length = length_collatz_sequence(starting_number);
		if(length > maximum_length) {
			maximum_length = length;
			maximum_starting_number = starting_number;
		}
	}
	printf("%u\n", maximum_starting_number);
}
