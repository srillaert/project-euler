#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX_ARRAY_SIZE 100

unsigned int max(unsigned int a, unsigned int b) {
    return a > b ? a : b;
}

unsigned int get_maximum_path_sum(char *filename) {
    FILE *stream;
    char c;
    unsigned int array[MAX_ARRAY_SIZE];

    // inspired by https://stackoverflow.com/questions/8465006/how-do-i-concatenate-two-strings-in-c
    char *start_command = "tac ";    
    char *command = malloc(strlen(start_command) + strlen(filename) + 1); // +1 for the null-terminator
    strcpy(command, start_command);
    strcat(command, filename);
    stream = popen(command, "r");
    free(command);

    // Read the first row into the array
    unsigned int number = 0;
    int i = 0;
    do {
        c = getc(stream);
        if(c >= '0' && c <= '9') {
            number = number * 10 + (c - '0');            
        } else {
            array[i++] = number;
            number = 0;
        }
    } while(c != '\n');

    // Update the array with the next rows
    number = 0;
    i = 0;
    while((c = getc(stream)) != EOF) {
        if(c >= '0' && c <= '9') {
            number = number * 10 + (c - '0');            
        } else {
            array[i] = max(array[i], array[i+1]) + number;
            i = c == '\n' ? 0 : i + 1;
            number = 0;
        }
    }
    pclose(stream);

    return array[0];
}
