#include<math.h>
#include<stdbool.h>
#include<stdio.h>

#define PANDIGITAL_MASK (1 << 10) - 2

int concat(int a, int b) {
	while(b > 0) {
		a = a * 10 + b % 10;
		b /= 10;
	}
	return a;
}

// Inspired by https://stackoverflow.com/questions/2484892/fastest-algorithm-to-check-if-a-number-is-pandigital
bool is_pandigital(int n) {
	int digits_mask = 0;
	while(n > 0) {
		int digit = n % 10;
		int previous = digits_mask;
		digits_mask |= 1 << digit;
		if (digits_mask == previous)
			return false;
		n /= 10;
	}
	return digits_mask == PANDIGITAL_MASK;
}

// Inspired by https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p032.py
bool is_pandigital_product(int n) {
	for(int i=2; i<sqrt(n)+1; i++) {
		if(n%i==0) {
			int identity = concat(concat(n, i), n/i);
			if(is_pandigital(identity))
				return true;
		}	
	}
	return false;
}

int main() {
	int result = 0;
	for(int i=1234; i<=9876; i++) {
		if(is_pandigital_product(i))
			result += i;
	}
	printf("%d\n", result);
}
