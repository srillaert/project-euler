#include <math.h>
#include <stdbool.h>
#include <stdio.h>

bool is_solution(unsigned long long n) {
	for(unsigned char d = 9; d > 1; d--) {
		if(n % 10 != d) return false;
		n /= 100;
	}
	return n == 1;
}

int main() {
	unsigned long long n = ((unsigned long long)sqrt(10203040506070809ULL) / 10) * 10 + 3;
	
	while(true) {
		if(is_solution(n*n)) break;
		n += 4; // ends with 7
		if(is_solution(n*n)) break;
		n += 6; // ends with 3 again
	}
	
	printf("%llu\n", n * 10);
}
