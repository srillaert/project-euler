#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define BUFFER_SIZE 46447 // size of the input file, we need less because the double quotes around the strings are removed

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
	char name_buffer[BUFFER_SIZE];

	// read the file into the string buffer
	FILE *stream = fopen("p022.input", "r");
	char c;
	int i = 0;
	int name_count = 1; // there is one name more than there are commas
	while((c = fgetc(stream)) != EOF) {
		switch(c) {
			case '"':
				break;
			case ',':
				name_buffer[i++] = '\0';
				name_count++;
				break;
			default:
				name_buffer[i++] = c;
				break;
		}
	}
	name_buffer[i] = '\0';
	fclose(stream);

	// build an array of string pointers to the names in the buffer
	char **names = malloc(name_count * sizeof(char*));
	char *name = name_buffer;
	for(int i=0; i<name_count; i++) {
		names[i] = name++;
		while(*(name++) != '\0');
	}

	// sort the names alphabetically
	qsort(names, name_count, sizeof(char*), pstrcmp);

	// finally calculate the score
	unsigned long total_name_scores = 0;
	for(int i=0; i<name_count; i++)
		total_name_scores += (i+1) * get_alphabetical_value(names[i]);

	free(names);
	return total_name_scores;
}

int main() {
	unsigned long result = get_total_name_scores();
	printf("%lu\n", result);
}

