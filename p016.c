#include<stdbool.h>
#include<stdio.h>
#include<stdint.h>

#define POWER_OF_TWO 1000
#define NUMBER_OF_BYTES (POWER_OF_TWO / 8) + 1
#define ONE_POSITION (POWER_OF_TWO) % 8

int main() {
	// initialize large_number to 2^POWER_OF_TWO, i.e., 2^1000
	uint8_t large_number[NUMBER_OF_BYTES];
	large_number[NUMBER_OF_BYTES - 1] = 1 << ONE_POSITION;
	for(int i=0; i<(NUMBER_OF_BYTES - 1); i++)
		large_number[i] = 0;

	int large_number_index = NUMBER_OF_BYTES - 1;
	uint16_t sum_decimal_digits = 0;
	while(true) {
		// divide large_number by 10
		uint8_t remainder = 0;
		for(int i=large_number_index; i>=0; i--) {
			uint16_t dividend = remainder * 256 + large_number[i];
			large_number[i] = dividend / 10;
			remainder = dividend % 10;
		}

		// add the remainder of the division by 10 to sum_decimal_digits
		sum_decimal_digits += remainder;

		if(large_number[large_number_index] == 0) { // can we reduce the array used for division ?
			if (large_number_index == 0) break; // we are done
			large_number_index--;
		}
	}

	printf("%u\n", sum_decimal_digits);
}
