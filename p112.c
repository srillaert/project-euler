#include <stdbool.h>
#include <stdio.h>

#define PERCENTAGE 99

enum state { Increasing, Decreasing, Equal };

bool is_bouncy_number(unsigned long n) {
	enum state current_state = Equal;
	unsigned int right_digit = n % 10;
	n /= 10;
	while(n > 0) {
		unsigned int left_digit = n % 10;
		n /= 10;
		if(left_digit > right_digit) {
			if(current_state == Decreasing) return true;
			current_state = Increasing;
		} else if(left_digit < right_digit) {
			if(current_state == Increasing) return true;
			current_state = Decreasing;
		}
		right_digit = left_digit;
	}
	return false;
}

int main() {
	unsigned long bouncy_numbers_count = 0;
	unsigned long n = 99;
	while((bouncy_numbers_count * 100 / n) < PERCENTAGE) {
		if(is_bouncy_number(++n)) bouncy_numbers_count++;	
	}
	printf("%lu\n", n);
}
