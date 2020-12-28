#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

#define TILL 20

uint_fast32_t get_least_common_multiple() {
	uint_fast8_t array[TILL];

	for(uint_fast8_t i = 0; i < TILL; i++) 
		array[i] = i + 1;

	uint_fast32_t lcm = 1;

	for(uint_fast8_t divisor = 2; divisor <= TILL; divisor++) {
		bool continue_search = true;
		while(continue_search) {
			continue_search = false;
			for(int i = 0; i < TILL; i++) {
				if(array[i] % divisor == 0) {
					array[i] /= divisor;
					continue_search = true;
				}
			}
			if(continue_search)
				lcm *= divisor;
		}
	}

	return lcm;
}

int main() {
	uint_fast32_t lcm = get_least_common_multiple();
	printf("%lu\n", lcm);
}

