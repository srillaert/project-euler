#include <stdio.h>
#include <stdint.h>

#define WIDTH_GRID 20
#define EMPTY_ARRAY_ELEMENT 0 // We use 0 to indicate an empty array element
#define SIZE_ARRAY WIDTH_GRID * 2 + 2 // We also need to leave a spot for the closing empty array element

void create_next_row(uint_fast64_t *previous, uint_fast64_t *next) {
	next[0] = 1;
	size_t i = 1;
	while(previous[i] != EMPTY_ARRAY_ELEMENT) {
		next[i] = previous[i-1] + previous[i];
		i++;
	}
	next[i] = 1;
	next[i+1] = EMPTY_ARRAY_ELEMENT;
}

int main() {
	uint_fast64_t a[SIZE_ARRAY] = { 1, 2, 1, EMPTY_ARRAY_ELEMENT };
	uint_fast64_t b[SIZE_ARRAY];

	for(uint_fast8_t i = 0; i < (WIDTH_GRID - 1); i++) {
		create_next_row(a, b);
		create_next_row(b, a);
	}

	uint_fast64_t middle_element = a[WIDTH_GRID];
	printf("%lu\n", middle_element);
}
