#include <stdint.h>
#include <stdio.h>

int main(void) {
	for(uint_fast32_t c = 334; c <= 998; c++) {
		uint_fast32_t b = c > 500 ? 999 - c : c - 1;
		uint_fast32_t a = 1000 - b - c;
		while(a <= b) {
			if(a*a + b*b == c*c) {
				printf("%lu\n", a*b*c);
				return 0;
			}
			a += 1;
			b -= 1;
		}
	}
}
