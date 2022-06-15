#include<stdio.h>

#define FIRST_POSITION 1
#define REMAINDER_TO_POSITION_NOT_SET 0 // 0 is not used since we start counting positions from 1
#define TILL_D 1000

// returns the length of the recurring cyle in the decimal fraction of 1/d
// returns 0 when there is no recurring cycle
int length_recurring_cycle(int d) {
	// initialize the array that holds the last position of the different remainders
	int remainder_to_position[TILL_D]; // there are d possible different remainders : 0, 1, ..., d-1.
	for(int i=0; i<TILL_D; i++)
		remainder_to_position[i] = REMAINDER_TO_POSITION_NOT_SET;

	int remainder = 1; // 1 is the number we divide
	int position = FIRST_POSITION;
	while(remainder_to_position[remainder] == REMAINDER_TO_POSITION_NOT_SET) {
		remainder_to_position[remainder] = position;

		// algorithm of long division
		do {
			remainder *= 10;
			position++;
		} while(remainder < d);
		remainder = remainder % d;

		if(remainder == 0) return 0; // there is no cycle
	}
	return position - remainder_to_position[remainder] + 1;
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
