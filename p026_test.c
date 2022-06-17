#include "p026_lib.c"
#include <stdio.h>

void assert(unsigned int expected, unsigned int actual, char* message) {
	if(expected != actual) {
		printf("expected %u but actual %u for %s\n", expected, actual, message);
	}
}

void assert_cycle(unsigned int divider, unsigned int cycle_length, char* message) {
	unsigned int actual = length_recurring_cycle(divider);
	assert(cycle_length, actual, message);
}

int main() {
	assert_cycle(2, 0, "1/2 = 0.5");
	assert_cycle(3, 1, "1/3 = 0.(3)");
	assert_cycle(333, 3, "1/333 = 0.(003)");
}
