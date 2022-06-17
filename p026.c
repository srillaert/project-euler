#include<stdio.h>
#include "p026_lib.c"

int main() {
	unsigned int d_longest_cycle = -1;
	unsigned int max_length = 0;
	for(unsigned int d=TILL_D; d>max_length /* dividend d can maximum have a cycle of length d */; d--) {
		unsigned int length = length_recurring_cycle(d);
		if(length > max_length) {
			max_length = length;
			d_longest_cycle = d;
		}
	}
	printf("%u\n", d_longest_cycle);
}
