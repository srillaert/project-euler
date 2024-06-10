#ifndef PRIME_SIEVE_H
#define PRIME_SIEVE_H

#include <stdbool.h>
#include <stdint.h>

#define SIEVE_WORD_TYPE uint32_t
#define SIEVE_WORD_MAX UINT32_MAX
#define SIEVE_WORD_BIT_LEN (sizeof(SIEVE_WORD_TYPE) * 8)

void prime_sieve_initialize(SIEVE_WORD_TYPE* sieve, uint_fast32_t size_sieve, uint_fast32_t exclusive_till);
bool prime_sieve_is_prime(SIEVE_WORD_TYPE* sieve, uint_fast32_t n);

#endif
