#include <stdio.h>

#define WIDTH_GRID 20
#define EMPTY_ARRAY_ELEMENT 0 // We use 0 to indicate an empty array element
#define SIZE_ARRAY WIDTH_GRID * 2 + 2 // We also need to leave a spot for the closing empty array element

void create_next_row(unsigned long long *previous, unsigned long long *next) {
	next[0] = 1;
	int i = 1;
	while(previous[i] != EMPTY_ARRAY_ELEMENT) {
		next[i] = previous[i-1] + previous[i];
		i++;
	}
	next[i] = 1;
	next[i+1] = EMPTY_ARRAY_ELEMENT;
}

int main() {
	unsigned long long a[SIZE_ARRAY] = { 1, 2, 1, EMPTY_ARRAY_ELEMENT };
	unsigned long long b[SIZE_ARRAY];

	for(int i; i < (WIDTH_GRID - 1); i++) {
		create_next_row(a, b);
		create_next_row(b, a);
	}

	//for(int i; i < SIZE_ARRAY; i++)
	//	printf("%llu ", a[i]);

	unsigned long long middle_element = a[WIDTH_GRID];

	printf("%llu\n", middle_element);
}
