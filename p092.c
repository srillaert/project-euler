#include<stdio.h>

int next_number(int number) {
	int sum = 0;
	while(number > 0) {
		int digit = number % 10;
		sum += digit * digit;
		number /= 10;
	}
	return sum;
}

int main() {
	int result = 0;
	for(int i = 1; i < 10000000; i++) {
		int number = i;
		while (number != 1 && number != 89) {
			number = next_number(number);
		}
		if (number == 89)
			result++;
	}
	printf("%d\n", result);
}
