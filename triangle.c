#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX_LINE_COUNT 100 // Maximum number of lines in the triangle file

unsigned int max(unsigned int a, unsigned int b) {
    return a > b ? a : b;
}

unsigned int get_maximum_path_sum(char *filename) {
    // Read the lines of the file in reverse order by using the Unix tac command
    char *start_command = "tac ";
    // inspired by https://stackoverflow.com/questions/8465006/how-do-i-concatenate-two-strings-in-c
    char *command = malloc(strlen(start_command) + strlen(filename) + 1); // +1 for the null-terminator
    strcpy(command, start_command);
    strcat(command, filename);
    FILE *stream;
    stream = popen(command, "r");
    free(command);

    // Read the bottom of the triangle into the array
    unsigned int number = 0;
    int i = 0;
    char c;
    unsigned int max_path_subtriangle[MAX_LINE_COUNT];
    do {
        c = getc(stream);
        if(c >= '0' && c <= '9') {
            number = number * 10 + (c - '0');            
        } else {
            max_path_subtriangle[i++] = number;
            number = 0;
        }
    } while(c != '\n');

    // Update the array while reading to the top of the triangle
    number = 0;
    i = 0;
    while((c = getc(stream)) != EOF) {
        if(c >= '0' && c <= '9') {
            number = number * 10 + (c - '0');            
        } else {
            // Keep the invariant that an array element contains the maximum path of a subtriangle
            max_path_subtriangle[i] = max(max_path_subtriangle[i], max_path_subtriangle[i+1]) + number;
            i = c == '\n' ? 0 : i + 1;
            number = 0;
        }
    }
    pclose(stream);

    // Because of the invariant element 0 contains the maximum path sum of the whole triangle
    return max_path_subtriangle[0];
}
