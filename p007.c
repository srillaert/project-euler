#include <math.h>
#include <stdio.h>

int is_prime(unsigned int n) {
	unsigned int till = sqrt(n);
	for(unsigned int i = 3; i <= till; i+=2)
		if(n%i == 0)
			return 0;
	return 1;
}


int main() {
	unsigned int number = 1;
	for(unsigned int count = 1; count < 10001;) {
		number += 2;
		if(is_prime(number))
			count++;
	}
	printf("%u\n", number);
}
