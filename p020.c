#include<stdio.h>

#define ARRAY_SIZE 100 // factorial(100) is smaller than a 2 * 100 digit number
#define FACTORIAL_OF 100

int main() {
	// Put the number 1 in the array
	unsigned int array[ARRAY_SIZE] = { 1 };
	int till_index = 0;

	// Calculate the factorial	
	for(unsigned int m = 2; m <= FACTORIAL_OF; m++) {
		unsigned int transfer = 0;
		for(int i = 0; i <= till_index; i++) {
			unsigned int product = array[i] * m + transfer;
			transfer = product / 100;
			array[i] = product % 100;
		}
		if(transfer > 0) array[++till_index] = transfer;
	}

	// Calculate the sum of the digits and print it out
	unsigned int sum_digits = 0;
	for(int i = till_index; i >= 0; i--)
		sum_digits += array[i] % 10 + (array[i] / 10) % 10;
	printf("%u\n", sum_digits);
}
