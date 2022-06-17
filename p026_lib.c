#define FIRST_POSITION 1
#define REMAINDER_TO_POSITION_NOT_SET 0 // 0 is not used since we start counting positions from 1
#define TILL_D 1000

// returns the length of the recurring cyle in the decimal fraction of 1/d
// returns 0 when there is no recurring cycle
unsigned int length_recurring_cycle(unsigned int d) {
	// initialize the array that holds the last position of the different remainders
	unsigned int remainder_to_position[TILL_D]; // there are d possible different remainders : 0, 1, ..., d-1.
	for(unsigned int i=0; i<TILL_D; i++)
		remainder_to_position[i] = REMAINDER_TO_POSITION_NOT_SET;

	unsigned int remainder = 1; // 1 is the number we divide
	unsigned int position = FIRST_POSITION;
	do {
		remainder_to_position[remainder] = position;

		// algorithm of long division
		do {
			remainder *= 10;
			position++;
		} while(remainder < d);
		remainder = remainder % d;

		if(remainder == 0) return 0; // there is no cycle
	} while(remainder_to_position[remainder] == REMAINDER_TO_POSITION_NOT_SET);
	return position - remainder_to_position[remainder];
}
