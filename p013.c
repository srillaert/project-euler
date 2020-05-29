#include <stdio.h>

int main() {
	FILE *stream;
	char line[50];
	unsigned int sum[52];

	// initialize the sum to 0
	for(int i=0; i<52; i++)
		sum[i] = 0;

	// add the digits from the file
	stream = fopen("p013.input", "r");
	while(fscanf(stream, "%s", line) == 1) {
		for(int i=0; i<50; i++)
			sum[i+2] += line[i] - '0';
	}	
	fclose(stream);

	// make the result decimal
	for(int i=51; i>0; i--) {
		sum[i-1] += sum[i] / 10;
		sum[i] = sum[i] % 10;
	}

	// print out the first 10 digits
	for(int i=0; i<10; i++)
		printf("%u", sum[i]);
	printf("\n");
}
