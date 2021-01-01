#include <stdio.h>
#include <stdint.h>

#define LENGTH_TYPE uint32_t // Can be an uint16_t in practice because the maximum length we find is 525 but how can we know this a priori ?
#define NUMBER_TYPE uint32_t // TILL is 1 million
#define OUTPUT_NOT_YET_KNOWN 0 // We use 0 to indicate that we don't have the output of this function input yet
#define TILL 1000000

LENGTH_TYPE memoization_array[TILL];

void initialize_memoization_array() {
	memoization_array[1] = 1;
	for(NUMBER_TYPE i = 2; i < TILL; i++)
		memoization_array[i] = OUTPUT_NOT_YET_KNOWN;
}

LENGTH_TYPE length_collatz_sequence(NUMBER_TYPE n) {
	if (n < TILL) {
		LENGTH_TYPE memoization = memoization_array[n];
		if(memoization != OUTPUT_NOT_YET_KNOWN)
			return memoization;
	}

	LENGTH_TYPE length = 
		n % 2 == 0 ?
			length_collatz_sequence(n / 2) + 1 : // n is even
			length_collatz_sequence((3 * n + 1) / 2) + 2; // n is odd, then 3*n+1 is even on which we can apply immediately the next step of dividing by 2
	if (n < TILL)
		memoization_array[n] = length;	
	return length;
}

int main(void) {
	initialize_memoization_array();

	// Go over the starting numbers and find the one with the maximum length
	LENGTH_TYPE maximum_length = 0;
	NUMBER_TYPE maximum_starting_number = 0;
	for(NUMBER_TYPE starting_number = 1; starting_number < TILL; starting_number++) {
		LENGTH_TYPE length = length_collatz_sequence(starting_number);
		if(length > maximum_length) {
			maximum_length = length;
			maximum_starting_number = starting_number;
		}
	}
	
	printf("%u\n", maximum_starting_number);
}
