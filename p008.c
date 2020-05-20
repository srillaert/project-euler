#include<stdio.h>

#define LENGTH 13

int main() {
	FILE *fp;
	char digits[LENGTH];
	for(int i=0; i<LENGTH; i++)
		digits[i] = 0;
	int digits_insert_position = 0;

	fp = fopen("p008.input", "r");
	char c;
	unsigned long long greatest_product = 0;
	while((c = fgetc(fp)) != EOF)
		if(c != '\n') {
			digits[digits_insert_position] = c - '0';
			digits_insert_position = (digits_insert_position + 1) % LENGTH;
			unsigned long long product = 1;
			for(int i=0; i<LENGTH; i++)
				product *= digits[i];
			if (product > greatest_product)
				greatest_product = product;
		}
	fclose(fp);

	printf("%llu\n", greatest_product);
}
