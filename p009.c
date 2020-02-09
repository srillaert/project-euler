#include <stdio.h>

int main(void) {
	for(unsigned int c = 334; c <= 998; c++) {
		unsigned int b = c > 500 ? 999 - c : c - 1;
		unsigned int a = 1000 - b - c;
		while(a <= b) {
			if(a*a + b*b == c*c) {
				//printf("a = %u, b = %u, c = %u\n", a, b, c);
				printf("%u\n", a*b*c);
				return 0;
			}
			a += 1;
			b -= 1;
		}
	}
}
