#include<stdbool.h>
#include<stdio.h>

#define TILL 1000000

bool is_prime[TILL];

void initialize_sieve_of_eratosthenes() {
	for(int i=2; i<TILL; i++) 
		is_prime[i] = true;
	for(int i=2; i<(TILL/2); i++)
		if(is_prime[i] == true)
			for(int multiple=i*2; multiple<TILL; multiple+=i)
				is_prime[multiple] = false;
}

int main() {
	initialize_sieve_of_eratosthenes();

	int result = 1; // 2 is a circular prime but we don't include it in the loop later
	int first_digit_factor = 1;
	for(int n=3; n<TILL; n+=2) {
		if(is_prime[n] == true) {
			if(n > first_digit_factor*10) first_digit_factor *= 10;
			int rotate = n;
			int all_prime = true;
			do {
				int first_digit = rotate % 10;
				rotate = first_digit * first_digit_factor + rotate / 10;
				if(is_prime[rotate] == false)
					all_prime=false;
			} while(all_prime == true && rotate != n);
			if(all_prime == true)
				result++;
		}
	}
	printf("%d\n", result);
}
