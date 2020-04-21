#include<stdbool.h>
#include<stdio.h>

#define NUMBER_LIMIT 10000000
#define CACHE_LIMIT 9*9*7 // number with the highest square digit is 9999999

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
	bool arrives_at_89[CACHE_LIMIT + 1];

	for(int i = 1; i <= CACHE_LIMIT; i++) {
		int number = i;
		while(1) {
			if(number == 1) {
				arrives_at_89[i] = false;
				break;
			} else if(number == 89) {
				arrives_at_89[i] = true;
				result++;
				break;
			}
			number = next_number(number);
		}
	}

	for(int i = CACHE_LIMIT + 1; i < NUMBER_LIMIT; i++) {
		int number = next_number(i);
		if(arrives_at_89[number])
			result++;
	}
	printf("%d\n", result);
}
