#include<math.h>
#include<stdio.h>

#define TARGET 4

int distinct_prime_factors_count(int n) {
	int count = 0;
	int till = ceil(sqrt(n));
	for(int d=2; d<=till; d++) {
		if(n % d != 0)
			continue;
		count++;
		do {
			n /= d;
		} while(n % d == 0);
		till = ceil(sqrt(n));
	}
	if(n != 1)
		count++;
	return count;
}

int main() {
	int consecutive_count = 0;
	int n = 1;
	while(consecutive_count < TARGET) {
		consecutive_count = 
			distinct_prime_factors_count(++n) == TARGET ? 
				consecutive_count + 1 :
				0;
	}
	int first_integer = n - TARGET + 1;
	printf("%d\n", first_integer);
}
