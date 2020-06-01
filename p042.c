#include<stdio.h>
#include<stdbool.h>

#define ARRAY_SIZE 1000

bool is_triangle_number[ARRAY_SIZE];

void initialize_lookup_array() {
	for(int i = 0; i < ARRAY_SIZE; i++)
		is_triangle_number[i] = false;
	int triangle_number = 1;
	for(int n = 2; triangle_number < ARRAY_SIZE; triangle_number += n++) {
		is_triangle_number[triangle_number] = true;
	}
}

int calculate_result() {
	FILE *stream;
	char c;
	int result = 0;

	stream = fopen("p042.input", "r");
	// calculate the result, the number of words with a word value that is a triangle number
	do {
		fgetc(stream); // starting "
		int word_value = 0;
		while((c = fgetc(stream)) != '"') // word letters and closing "
			word_value += c - 'A' + 1;
		if(is_triangle_number[word_value]) 
			result += 1;
	} while(fgetc(stream) != EOF); // EOF or comma
	fclose(stream);
	return result;
}

int main() {
	initialize_lookup_array();
	int result = calculate_result();
	printf("%d\n", result);
}

