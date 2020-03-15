#include <stdbool.h>
#include <stdio.h>

#define TILL 28123

int main() {
	// create an array with the sum of the proper divisors of each number
	int sum_proper_divisors[TILL + 1];
	// initialize the array with 1s because all the numbers have 1 as a proper divisor
	for(int i=1; i<=TILL; i++)
		sum_proper_divisors[i] = 1;
	// add all the proper divisors greater than 1
	for(int divisor=2; divisor<=TILL/2; divisor++)
		for(int multiple=2*divisor; multiple<=TILL; multiple+=divisor)
			sum_proper_divisors[multiple] += divisor;

	// create an array with abundant numbers that is quick to iterate over
	int abundant_numbers[TILL];
	int add_location = 0;
	for(int i=2; i<=TILL; i++)
		if(sum_proper_divisors[i] > i)
			abundant_numbers[add_location++] = i;
	abundant_numbers[add_location] = -1;

	// create an boolean array indicating which numbers are a sum of two abundant numbers
	bool is_sum[TILL + 1];
	for(int i=0; i<=TILL; i++)
		is_sum[i] = false;	
	for(int i=0; abundant_numbers[i] != -1; i++)
		for(int j=i; abundant_numbers[j] != -1; j++) {
			int sum = abundant_numbers[i] + abundant_numbers[j];
			if (sum > TILL) break;
			is_sum[sum] = true;
		}

	// calculate the result
	int result = 0;
	for(int i=0; i<=TILL; i++)
		if(is_sum[i] == false)
			result += i;

	printf("%d\n", result);
}
