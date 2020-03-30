#include<stdio.h>

#define TILL_D 1000
int remainders[TILL_D]; // There cannot be more different remainders than d, the dividend

int length_recurring_cycle(int d) {
	int remainder = 1;	
	for(int i=0; i<TILL_D; i++) {
		remainders[i] = remainder;
		do {
			remainder *= 10;
		} while(remainder < d);
		remainder = remainder % d;
		if(remainder == 0)
			return 0;
		for(int j=i; j>0; j--) {
			if(remainders[j] == remainder)
				return i-j+1;
		}
	}
}

int main() {
	int d_longest_cycle = -1;
	int max_length = 0;
	for(int d=TILL_D-1; d>max_length /* dividend d can maximum have a cycle of length d */; d--) {
		int length = length_recurring_cycle(d);
		if(length > max_length) {
			max_length = length;
			d_longest_cycle = d;
		}
	}
	printf("%d\n", d_longest_cycle);
}
