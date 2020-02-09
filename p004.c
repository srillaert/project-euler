#include <stdio.h>

int reverse(int n) {
	int result = 0;
	while(n > 0) {
		result = result * 10 + n % 10;
		n /= 10;
	}
	return result;
}

int main() {
	int largest = 0;
	for(int a = 999; a >= 100; a--) {
		for(int b = 999; b >= a; b--) {
			int product = a * b;
			if(product < largest)
				break;
			if(product == reverse(product))
				largest = product;
		}
	}
	printf("%d\n", largest);
}
