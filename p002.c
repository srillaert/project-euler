#include <stdio.h>

int main(void) {
	int former_term = 1;
	int latter_term = 1;
	int sum_even_valued_terms = 0;
	while(latter_term <= 4000000) {
		if(latter_term%2 == 0) 
			sum_even_valued_terms += latter_term;	
		int new_term = former_term + latter_term;
		former_term = latter_term;
		latter_term = new_term;
	}; 
	printf("%d\n", sum_even_valued_terms);
}
