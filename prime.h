#ifndef PRIME_H
#define PRIME_H

#include <stdbool.h>
#include <stdint.h>

void prime_sieve_initialize(uint8_t* sieve, uint_fast32_t size_sieve, uint_fast32_t exclusive_till);
bool prime_sieve_is_prime(uint8_t* sieve, uint_fast32_t n);

#endif
