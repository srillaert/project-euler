#include <stdio.h>

#define GRID_WIDTH 20
#define GRID_SIZE GRID_WIDTH * GRID_WIDTH

unsigned int numbers[GRID_SIZE];
unsigned int maximum = 0;

void update_maximum(int i, int step) {
	unsigned int product = 1;
	for(int j = i; j != (i + 4 * step); j += step)
		product *= numbers[j];
	if(product > maximum)
		maximum = product;
}

int main() {
	// Read input file
	FILE *input_file;
	input_file = fopen("p011.input", "r");
	unsigned int *current = numbers;
	while(fscanf(input_file, "%u", current++) == 1);

	// Find maximum
	for(int i = 0; i < GRID_SIZE; i++) {
		if(i % GRID_WIDTH <= (GRID_WIDTH - 4)) {
			update_maximum(i, +1); // horizontal right
			if(i >= 3 * GRID_WIDTH) update_maximum(i, -GRID_WIDTH + 1); // diagonal right up
			if(i < (GRID_WIDTH - 3) * GRID_WIDTH) update_maximum(i, +GRID_WIDTH + 1); // diagonal right down
		}
		if(i < (GRID_WIDTH - 3) * GRID_WIDTH) update_maximum(i, +GRID_WIDTH); // vertical down
	}

	// Print out result
	printf("%u\n", maximum);
}	
