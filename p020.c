#include<stdint.h>
#include<stdio.h>

#define ARRAY_SIZE 100 // factorial(100) is smaller than a 2 * 100 digit number
#define FACTORIAL_OF 100

// Print the sum of the decimal digits of FACTORIAL_OF!
int main() {
	uint8_t factorial_decimal_parts[ARRAY_SIZE] = { 1 }; // Put the number 1 in the array
	int highest_index_with_digits = 0;

	// Calculate the factorial	
	for(uint8_t m = 2; m <= FACTORIAL_OF; m++) {
		uint8_t transfer = 0;
		for(int i = 0; i <= highest_index_with_digits; i++) {
			uint16_t product = factorial_decimal_parts[i] * m + transfer;
			transfer = product / 100;
			factorial_decimal_parts[i] = product % 100;
		}
		if(transfer > 0) factorial_decimal_parts[++highest_index_with_digits] = transfer;
	}

	// Calculate the sum of the digits and print it out
	uint16_t sum_digits = 0;
	for(int i = highest_index_with_digits; i >= 0; i--)
		sum_digits += factorial_decimal_parts[i] % 10 + (factorial_decimal_parts[i] / 10) % 10;
	printf("%u\n", sum_digits);
}
