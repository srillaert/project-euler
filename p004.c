#include <stdint.h>
#include <stdio.h>

uint_fast32_t reverse(uint_fast32_t n) {
	uint_fast32_t result = 0;
	while(n > 0) {
		result = result * 10 + n % 10;
		n /= 10;
	}
	return result;
}

uint_fast32_t largest_palindrome_product() {
	uint_fast32_t largest_palindrome = 0;
	for(uint_fast16_t a = 999; a >= 100; a--) {
		for(uint_fast16_t b = 999; b >= a; b--) {
			uint_fast32_t product = a * b;
			if(product <= largest_palindrome)
				break;
			if(product == reverse(product))
				largest_palindrome = product;
		}
	}
	return largest_palindrome;
}

int main() {
	uint_fast32_t solution = largest_palindrome_product();
	printf("%lu\n", solution);
}
