#include <stdio.h>
#include <stdint.h>

#define GRID_WIDTH 20
#define GRID_SIZE GRID_WIDTH * GRID_WIDTH

uint_fast8_t numbers[GRID_SIZE];
uint_fast32_t maximum = 0;

void update_maximum(int i, int step) {
	uint_fast32_t product = 1;
	for(int j = i; j != (i + 4 * step); j += step)
		product *= numbers[j];
	if(product > maximum)
		maximum = product;
}

int main() {
	// Read input file
	FILE *input_file;
	input_file = fopen("p011.input", "r");
	uint_fast8_t *current = numbers;
	while(fscanf(input_file, "%hhu", current++) == 1);
	fclose(input_file);

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
	printf("%lu\n", maximum);
}	
