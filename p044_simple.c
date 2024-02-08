#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>

uint32_t pentagonal(uint32_t n) {
    return n * (3 * n - 1) / 2;
}

// see https://en.wikipedia.org/wiki/Pentagonal_number#Tests_for_pentagonal_numbers
bool is_pentagonal(uint32_t n) {
    double r = sqrt(1 + 24 * n);
    double remainder = fmod(r, 6.0);
    double tolerance = 1e-10;
    bool result = fabs(remainder - 5.0) < tolerance;
    return result;
}

uint32_t solution() {
    uint32_t k = 2;
    while (true) {
        uint32_t pk = pentagonal(k);
        for (uint32_t j = k - 1; j > 0; j--) {
            uint32_t pj = pentagonal(j);
            if (is_pentagonal(pk + pj) && is_pentagonal(pk - pj)) {
                return pk - pj;
            }
        }
        k++;
    }
}

int main(void) {
    printf("%u\n", solution());
    return 0;
}