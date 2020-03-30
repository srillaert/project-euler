#include<stdio.h>

#define TILL_D 1000

int length_recurring_cycle(int d) {
	// Initialize the array
	int remainder_position[TILL_D]; // There are d possible different remainders : 0, 1, ..., d-1.
	for(int i=0; i<TILL_D; i++)
		remainder_position[i] = 0;

	int remainder = 1;
	int position = 1;
	while(remainder_position[remainder] == 0) {
		remainder_position[remainder] = position++;
		do {
			remainder *= 10;
		} while(remainder < d);
		remainder = remainder % d;
		if(remainder == 0)
			return 0;
	}
	return position - remainder_position[remainder] + 1;
}

int main() {
	int d_longest_cycle = -1;
	int max_length = 0;
	for(int d=TILL_D; d>max_length /* dividend d can maximum have a cycle of length d */; d--) {
		int length = length_recurring_cycle(d);
		if(length > max_length) {
			max_length = length;
			d_longest_cycle = d;
		}
	}
	printf("%d\n", d_longest_cycle);
}
