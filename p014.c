#include <stdio.h>

#define OUTPUT_NOT_YET_KNOWN 0 // We use 0 to indicate that we don't have the output of this function input yet
#define TILL 1000000

unsigned int memoization_array[TILL];

unsigned int length_collatz_sequence(unsigned int n) {
	if (n < TILL) {
		unsigned int memoization = memoization_array[n];
		if(memoization != OUTPUT_NOT_YET_KNOWN)
			return memoization;
	}

	unsigned int length = 
		n % 2 == 0 ?
			length_collatz_sequence(n / 2) + 1 : // n is even
			length_collatz_sequence(3 * n + 1) + 1; // n is odd
	if (n < TILL)
		memoization_array[n] = length;	
	return length;
}

int main(void) {
	// Initiliaze the memoization array
	memoization_array[1] = 1;
	for(int i = 2; i < TILL; i++)
		memoization_array[i] = OUTPUT_NOT_YET_KNOWN;

	// Go over the starting numbers and find the one with the maximum length
	unsigned int maximum_length = 0;
	unsigned int maximum_starting_number = 0;
	for(unsigned int starting_number = 1; starting_number < TILL; starting_number++) {
		unsigned int length = length_collatz_sequence(starting_number);
		if(length > maximum_length) {
			maximum_length = length;
			maximum_starting_number = starting_number;
		}
	}
	
	printf("%u\n", maximum_starting_number);
}
