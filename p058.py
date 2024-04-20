from itertools import count
from cached_trial_division import CachedTrialDivision

def get_square_spirals():
    cached_trial_division = CachedTrialDivision()
    primes_count = 0
    for n in count(1):
        side_length = 2 * n + 1
        bottom_right_corner = side_length * side_length
        current_add = 2 * n
        extra_primes_count = sum(
            1 for n in range(
                bottom_right_corner - 3 * current_add, 
                bottom_right_corner, # The bottom right diagonal is the odd squares series so its terms will not be prime, exclude them from the test
                current_add)
                if cached_trial_division.is_prime(n))
        primes_count += extra_primes_count
        numbers_count = 1 + 4 * n
        yield (primes_count, numbers_count, side_length)

# what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
def get_solution():
    return next(side_length for primes_count, numbers_count, side_length in get_square_spirals() 
                if primes_count * 100 // numbers_count < 10)

if __name__ == "__main__":
    print(get_solution())