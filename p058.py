from itertools import count
from prime import is_prime

primes_count = 0
for n in count(1):
    side_length = 2 * n + 1
    bottom_right_corner = side_length * side_length
    current_add = 2 * n
    extra_primes_count = sum(
        1 for n in range(
            bottom_right_corner - 3 * current_add, 
            bottom_right_corner, # exclude from the prime test the numbers on the bottom right diagonal, they are the odd squares so they will not be prime
            current_add) 
            if is_prime(n))
    primes_count += extra_primes_count
    numbers_count = 1 + 4 * n
    if primes_count * 100 // numbers_count < 10:
        print(side_length)
        break