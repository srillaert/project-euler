#include <math.h>
#include <stdio.h>

int main() {
    FILE *stream;
    float base, exponent;    
    float max_value = 0;
    unsigned int max_line = 0;

    stream = fopen("p099.input", "r");
    for(unsigned int line = 1; fscanf(stream, "%f,%f", &base, &exponent) == 2; line++) {
        float logarithm = logf(base) * exponent;
        if(logarithm > max_value) {
            max_value = logarithm;
            max_line = line;
        }
    }
    fclose(stream);

    printf("%u\n", max_line);
}