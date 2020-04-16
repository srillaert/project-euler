#include<stdio.h>

#define ONE_MILLION 1000000
#define TILL 100

int main() {
	int row[TILL+1];
	row[0] = 1;
	for(int i=1; i<=TILL; i++)
		row[i] = 0;

	int count = 0;
	for(int n=1; n<=TILL; n++) {
		for(int r=n; r>0; r--) {
			int new_value = row[r] + row[r-1];
			if(new_value > ONE_MILLION) {
				new_value = ONE_MILLION; // We are not interested in the exact values above one million, prevent overflow of int
				count++;
			}
			row[r] = new_value;
		}
	}
	
	printf("%d\n", count);
}
