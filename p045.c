#include<stdio.h>

#define LOWER_LIMIT 40755

int main() {
	int triangle_number = 0;
	int pentagonal_number = 0; 
	int hexagonal_number = 0;

	int triangle_add = 1;
	int pentagonal_add = 1;
	int hexagonal_add = 1;

	do {
		hexagonal_number += hexagonal_add;
		hexagonal_add += 4;

		do {
			pentagonal_number += pentagonal_add;
			pentagonal_add += 3;
		} while(pentagonal_number < hexagonal_number);

		do {
			triangle_number += triangle_add;
			triangle_add += 1;
		} while(triangle_number < hexagonal_number);
	} while(hexagonal_number <= LOWER_LIMIT || pentagonal_number != hexagonal_number || triangle_number != hexagonal_number);

	printf("%d\n", hexagonal_number);
}
