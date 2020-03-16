#include <stdio.h>

int factorial[10];

void precalculate_factorials() {
	factorial[0] = factorial[1] = 1;
	for(int i=2; i<10; i++)
		factorial[i] = factorial[i-1] * i;
}

int is_curious_number(int n) {
	int v = n;
	int sum = 0;
	while(v>0) {
		int digit = v % 10;
		sum += factorial[digit];
		v /= 10;
	}
	return sum == n;
}

int main() {
	precalculate_factorials();

	int till = factorial[9] * 7; // 9! = 362.880 so with 7 digits the sum with the factorials of the digits can only we a 7 digit number 9! * 7 = 2.540.160
	int result = 0;
	for(int i = 10; i<=till; i++)
		if(is_curious_number(i))
			result += i;

	printf("%d\n", result);
}
