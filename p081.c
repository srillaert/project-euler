#include <stdio.h>

#define SIDE_MATRIX 80

unsigned long matrix[SIDE_MATRIX][SIDE_MATRIX];

unsigned long min(unsigned long a, unsigned long b) {
    return a < b ? a : b;
}

void read_matrix_from_file() {
    FILE *stream;    
    stream = fopen("p081.input", "r");
    int i = 0;
    unsigned long number = 0;
    char c;
    while((c = fgetc(stream)) != EOF) {
        if(c >= '0' && c <= '9')
            number = number * 10 + (c - '0');
        else if(number != 0) {
            matrix[i / SIDE_MATRIX][i % SIDE_MATRIX] = number;
            i++;
            number = 0;
        }
    }
    fclose(stream);
}

int main() {
    read_matrix_from_file();

    for(int row = 1; row < SIDE_MATRIX; row++)
        matrix[row][0] += matrix[row-1][0];
    for(int column = 1; column < SIDE_MATRIX; column++) {
        matrix[0][column] += matrix[0][column-1];
        for(int row = 1; row < SIDE_MATRIX; row++) {
            matrix[row][column] += min(matrix[row-1][column], matrix[row][column-1]);
        }
    }

    printf("%lu\n", matrix[SIDE_MATRIX-1][SIDE_MATRIX-1]);
}