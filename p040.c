#include <stdio.h>

#define TILL 1000000

int main(void) {
	char fractional_part[TILL + 10]; // 10 extra to leave some space for the end of the last integer
	
	char *current_position = fractional_part;
	for(int i=1; current_position <= fractional_part + TILL; i++) {
		int number_digits_written = sprintf(current_position, "%d", i);
		current_position += number_digits_written;
	}

	int product = 1;	
	for(int i=1; i<=TILL; i*=10) {
		product *= fractional_part[i-1] - '0';
	}
	printf("%d\n", product);
}
