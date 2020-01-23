#include <stdio.h>

int main(void) {
	int former_term = 1;
	int latter_term = 1;
	int new_term;
	int sum_even_valued_terms = 0;
	do {
		new_term = former_term + latter_term;
		if(new_term%2 == 0) 
			sum_even_valued_terms += new_term;	
		former_term = latter_term;
		latter_term = new_term;
	} while(new_term <= 4000000);
	printf("%d\n", sum_even_valued_terms);
}
