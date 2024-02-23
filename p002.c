#include <stdint.h>
#include <stdio.h>

int main(void) {
	uint_fast32_t former_fibonacci_number = 0;
	uint_fast32_t latter_fibonacci_number = 1;
	uint_fast32_t sum_even_fibonacci_numbers = 0;
	while(latter_fibonacci_number <= 4000000) {
		if(latter_fibonacci_number%2 == 0) 
			sum_even_fibonacci_numbers += latter_fibonacci_number;	
		uint_fast32_t new_term = former_fibonacci_number + latter_fibonacci_number;
		former_fibonacci_number = latter_fibonacci_number;
		latter_fibonacci_number = new_term;
	}; 
	printf("%lu\n", sum_even_fibonacci_numbers);
}
