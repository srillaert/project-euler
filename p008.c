#include<stdio.h>
#include<stdint.h>

#define LENGTH 13

int main() {
	FILE *stream;
	uint_fast8_t digits[LENGTH];
	for(size_t i=0; i<LENGTH; i++)
		digits[i] = 0;
	size_t digits_insert_position = 0;

	stream = fopen("p008.input", "r");
	char c;
	uint_fast64_t greatest_product = 0;
	while((c = fgetc(stream)) != EOF)
		if(c != '\n') {
			digits[digits_insert_position] = c - '0';
			digits_insert_position = (digits_insert_position + 1) % LENGTH;
			uint_fast64_t product = 1;
			for(size_t i=0; i<LENGTH; i++)
				product *= digits[i];
			if (product > greatest_product)
				greatest_product = product;
		}
	fclose(stream);

	printf("%lu\n", greatest_product);
}
