#include <stdint.h>
#include <stdio.h>

int main(void) {
	uint_fast32_t former_term = 1;
	uint_fast32_t latter_term = 1;
	uint_fast32_t sum_even_valued_terms = 0;
	while(latter_term <= 4000000) {
		if(latter_term%2 == 0) 
			sum_even_valued_terms += latter_term;	
		uint_fast32_t new_term = former_term + latter_term;
		former_term = latter_term;
		latter_term = new_term;
	}; 
	printf("%lu\n", sum_even_valued_terms);
}
