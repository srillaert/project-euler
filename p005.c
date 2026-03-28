#include <stdint.h>
#include <stdio.h>

#define TILL 20

uint_fast32_t get_least_common_multiple() {
	uint_fast32_t lcm = 1;
	uint_fast8_t n[TILL];
	for(int i = 0; i < TILL; i++) n[i] = i + 1;
	for(int i = 0; i < TILL; i++) {
		if(n[i] != 1) {
			uint_fast8_t prime = n[i];
			lcm *= prime;
			for(int j = i+1; j < TILL; j+=1) if(n[j] % prime == 0) n[j] /= prime;
		}
	}
	return lcm;
}

int main() {
	uint_fast32_t lcm = get_least_common_multiple();
	printf("%lu\n", lcm);
}
