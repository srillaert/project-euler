#include<stdio.h>

#define POWER_OF_TWO 1000
#define NUMBER_OF_BYTES (POWER_OF_TWO / 8) + 1
#define ONE_POSITION (POWER_OF_TWO) % 8

int main() {
	unsigned char parts[NUMBER_OF_BYTES];
	parts[NUMBER_OF_BYTES - 1] = 1 << ONE_POSITION;
	for(int i=0; i<(NUMBER_OF_BYTES - 1); i++)
		parts[i] = 0;
	int part_index = NUMBER_OF_BYTES - 1;
	unsigned int result = 0;

	while(part_index > -1) {
		unsigned int remainder = 0;
		for(int i=part_index; i>=0; i--) {
			unsigned int dividend = remainder * 256 + parts[i];
			parts[i] = dividend / 10;
			remainder = dividend % 10;
		}
		result += remainder;
		if(parts[part_index] == 0)
			part_index--;
	}

	printf("%u\n", result);
}
