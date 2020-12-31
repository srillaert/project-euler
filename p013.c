#include <stdio.h>
#include <stdint.h>

int main() {
	FILE *stream;
	char line[50];
	uint_fast16_t sum[52]; // element can be maximum 9 * 50 = 450

	// initialize the sum to 0
	for(size_t i=0; i<52; i++)
		sum[i] = 0;

	// add the digits from the file
	stream = fopen("p013.input", "r");
	while(fscanf(stream, "%s", line) == 1) {
		for(size_t i=0; i<50; i++)
			sum[i+2] += line[i] - '0';
	}	
	fclose(stream);

	// make the result decimal
	for(size_t i=51; i>0; i--) {
		sum[i-1] += sum[i] / 10;
		sum[i] = sum[i] % 10;
	}

	// print out the first 10 digits
	for(size_t i=0; i<10; i++)
		printf("%lu", sum[i]);
	printf("\n");
}
