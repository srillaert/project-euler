#include<stdio.h>
#include<stdint.h>

#define NUMBER_OF_ADJACENT_DIGITS 13

int main() {
	FILE *stream;
	uint_fast8_t adjacent_digits[NUMBER_OF_ADJACENT_DIGITS];
	for(size_t i=0; i<NUMBER_OF_ADJACENT_DIGITS; i++)
		adjacent_digits[i] = 0;
	size_t digits_insert_position = 0;

	stream = fopen("p008.input", "r");
	char c;
	uint_fast64_t greatest_digits_product = 0;
	while((c = fgetc(stream)) != EOF) {
		if(c == '\n') continue; // ignore the newlines between parts of the number in the input file
		adjacent_digits[digits_insert_position] = c - '0';
		digits_insert_position = (digits_insert_position + 1) % NUMBER_OF_ADJACENT_DIGITS;
		uint_fast64_t digits_product = 1;
		for(size_t i=0; i<NUMBER_OF_ADJACENT_DIGITS; i++)
			digits_product *= adjacent_digits[i];
		if (digits_product > greatest_digits_product)
			greatest_digits_product = digits_product;
	}
	fclose(stream);

	printf("%lu\n", greatest_digits_product);
}
