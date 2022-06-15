#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

// From problem description : "By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit."
#define TILL 28123

int main() {
	// create an array with the sum of the proper divisors of each number
	uint32_t sum_proper_divisors[TILL + 1];
	// initialize the array with 1s because all the numbers have 1 as a proper divisor
	for(uint16_t i=1; i<=TILL; i++)
		sum_proper_divisors[i] = 1;
	// add all the proper divisors greater than 1
	for(uint16_t divisor=2; divisor<=TILL/2; divisor++)
		for(uint16_t multiple=2*divisor; multiple<=TILL; multiple+=divisor)
			sum_proper_divisors[multiple] += divisor;

	// create an array with abundant numbers that is quick to iterate over
	uint16_t abundant_numbers[TILL];
	uint16_t abundant_numbers_count = 0;
	for(uint16_t i=2; i<=TILL; i++)
		if(sum_proper_divisors[i] > i)
			abundant_numbers[abundant_numbers_count++] = i;

	// create an boolean array indicating which numbers are a sum of two abundant numbers
	bool is_sum[TILL + 1];
	for(uint16_t i=0; i<=TILL; i++)
		is_sum[i] = false;	
	for(uint16_t i=0; i<abundant_numbers_count; i++)
		for(uint16_t j=i; j<abundant_numbers_count; j++) {
			uint16_t sum = abundant_numbers[i] + abundant_numbers[j];
			if (sum > TILL) break;
			is_sum[sum] = true;
		}

	// calculate the result, the sum of the positive integers that cannot be expressed as the sum of two abundant numbers
	uint32_t result = 0;
	for(uint16_t i=0; i<=TILL; i++)
		if(is_sum[i] == false)
			result += i;

	printf("%u\n", result);
}
