#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define BUFFER_SIZE 46447 // size of the input file, we need less

unsigned int get_alphabetical_value(char* name) {
	unsigned int value = 0;
	do {
		value += *(name++) - 'A' + 1;
	} while(*name != '\0');
	return value;
}

int pstrcmp(const void* a, const void* b) {
	return strcmp(*(const char**)a, *(const char**)b);
}

unsigned long get_total_name_scores() {
	char buffer[BUFFER_SIZE];

	// read the file into the string buffer
	FILE *stream = fopen("p022.input", "r");
	char c;
	int i = 0;
	int word_count = 1; // there is one word more than there are commas
	while((c = fgetc(stream)) != EOF) {
		switch(c) {
			case '"':
				break;
			case ',':
				buffer[i++] = '\0';
				word_count++;
				break;
			default:
				buffer[i++] = c;
				break;
		}
	}
	buffer[i] = '\0';
	fclose(stream);

	// build an array of string pointers to the names in the buffer
	char **names = malloc(word_count * sizeof(char*));
	char *name = buffer - 1;
	for(int i=0; i<word_count; i++) {
		names[i] = name + 1;
		while(*(++name) != '\0');	
	}

	// sort the names alphabetically
	qsort(names, word_count, sizeof(char*), pstrcmp);

	// finally calculate the score
	unsigned long total_name_scores = 0;
	for(int i=0; i<word_count; i++)
		total_name_scores += (i+1) * get_alphabetical_value(names[i]);

	free(names);
	return total_name_scores;
}

int main() {
	unsigned long result = get_total_name_scores();
	printf("%lu\n", result);
}

