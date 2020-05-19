#include<stdio.h>

#define LENGTH 13

int main() {
    FILE *fp;
    char digits[1000];

    fp = fopen("p008.input", "r");
    char c;
    int i = 0;
    while((c = fgetc(fp)) != EOF)
        if(c != '\n')
            digits[i++] = c - '0';
    fclose(fp);

    unsigned long long greatest_product = 0;
    for(int i = 0; i < 1000 - LENGTH; i++) {
        unsigned long long product = 1;
        for(int j = i; j < i + LENGTH; j++)
            product *= digits[j];
        if (product > greatest_product)
            greatest_product = product;
    }

    printf("%llu\n", greatest_product);
}