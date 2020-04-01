#include<stdio.h>

#define TILL 1001

int main() {
	int max_solutions = -1;
	int max_solutions_p = -1;

	for(int p=1; p<TILL; p++) {
		int number_solutions = 0;
		// a <= b < c and a + b + c == p
		for(int a=1; a<=(p/3); a++) {
			for(int b=a; b<((p-a)/2); b++) {
				int c = p-a-b;
				if(a*a + b*b == c*c)
					number_solutions++;
			}
		}
		if(number_solutions > max_solutions) {
			max_solutions = number_solutions;
			max_solutions_p = p;
		}
	}
	
	printf("%d\n", max_solutions_p);
}
