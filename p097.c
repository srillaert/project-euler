#include<stdio.h>

#define MODULO_DIVISOR 10000000000

int main() {
	unsigned long long number = 1;
	for(int i=0; i<7830457; i++) {
		number = (number * 2) % MODULO_DIVISOR;
	}
	number = (28433 * number + 1) % MODULO_DIVISOR;
	printf("%llu\n", number);
}
