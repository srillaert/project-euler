#include<stdbool.h>
#include<stdio.h>

bool equal_digits_count(int* a, int* b) {
	for(int i=0; i<10; i++) {
		if(a[i] != b[i])
			return false;
	}
	return true;
}

int* get_digits_count(int n, int* digits_count) {
	for(int i=0; i<10; i++)
		digits_count[i] = 0;
	while(n > 0) {
		int digit = n % 10;
		digits_count[digit]++;
		n /= 10;
	}
}

int main() {
	int digits_number[10];
	int digits_multiple[10];
	bool is_equal = false;
	int number=0;
	while(!is_equal) {
		number++;
		get_digits_count(number, digits_number);
		is_equal = true;
		for(int multiple=2*number; multiple<=6*number && is_equal; multiple+=number) {
			get_digits_count(multiple, digits_multiple);
			is_equal = equal_digits_count(digits_number, digits_multiple);
		}
	}	
	printf("%d\n", number);
}
