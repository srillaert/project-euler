#include <stdint.h>
#include <stdio.h>

int main() {
	uint_fast32_t sum = 0;
	for(uint_fast16_t i = 1; i < 1000; i++)
		if (i%3==0 || i%5==0)
			sum += i;
	printf("%lu\n", sum);
}
