#include<stdbool.h>
#include<stdio.h>


bool is_binary_palindrome(int n) {
	int reversed = 0;
	int rest = n;
	while(rest > 0) {
		reversed = reversed * 2 + (rest % 2);
		rest /= 2;
	}
	return reversed == n;
}

int make_base_10_palindrome(int n, bool has_odd_length) {
	int rest = n;
	if(has_odd_length)
		rest /= 10;
	while(rest > 0) {
		n = n * 10 + rest % 10;
		rest /= 10;
	}
	return n;
}

int sum_palindromic_numbers(bool has_odd_length) {
	int sum = 0;
	for(int i=1; i<1000; i++) {
		int base_10_palindrome = make_base_10_palindrome(i, has_odd_length);
		if(is_binary_palindrome(base_10_palindrome))
			sum += base_10_palindrome;
	}
	return sum;
}

int main() {
	int sum_odd_length = sum_palindromic_numbers(true);
	int sum_even_length = sum_palindromic_numbers(false);
	int result = sum_odd_length + sum_even_length;
	printf("%d\n", result);
}
