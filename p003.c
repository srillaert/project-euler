#include <math.h>
#include <stdio.h>

int main(void) {
	unsigned long long number = 600851475143; // 13195
	unsigned long long till = sqrt(number);
	unsigned long long n = 2;

	while(n <= till) {
		while(number % n == 0) {
			number = number / n;
			till = sqrt(number);
		}
		n += 1;
	}
	printf("%llu\n", number);
}
