#include <stdio.h>

#define TILL 20

unsigned int get_least_common_multiple() {
	unsigned int array[TILL];

	for(unsigned int i = 0; i < TILL; i++) 
		array[i] = i + 1;

	unsigned int lcm = 1;

	for(unsigned int divisor = 2; divisor <= TILL; divisor++) {
		int continue_search = 1;
		while(continue_search) {
			continue_search = 0;
			for(int i = 0; i < TILL; i++) {
				if(array[i] % divisor == 0) {
					array[i] /= divisor;
					continue_search = 1;
				}
			}
			if(continue_search)
				lcm *= divisor;
		}
	}

	return lcm;
}

int main() {
	unsigned int lcm = get_least_common_multiple();
	printf("%u\n", lcm);
}

