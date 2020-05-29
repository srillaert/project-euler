#include<stdio.h>

#define MAX_ARRAY_SIZE 100

unsigned int max(unsigned int a, unsigned int b) {
    return a > b ? a : b;
}

int main() {
    FILE *stream;
    char c;
    unsigned int array[MAX_ARRAY_SIZE];

    stream = popen("tac p018.input", "r");
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

    printf("%u\n", array[0]);
}