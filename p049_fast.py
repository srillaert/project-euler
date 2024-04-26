# Based on the comment of Vlad on https://web.archive.org/web/20171231183448/http://www.mathblog.dk/project-euler-49-arithmetic-sequences-primes-permutations/
from itertools import combinations
from prime_sieve import PrimeSieve

def get_arithmetic_sequences():
    till = 10000
    sieve = PrimeSieve(till)

    permutations = {}
    for d in range(1000, till):
        if sieve.is_prime(d):
            key = ''.join(sorted(str(d))) # Permutations get the same key
            value = permutations.get(key)
            if value == None:
                permutations[key] = [ d ]
            else:
                value.append(d)

    for key in permutations:
        for a, b, c in sorted(combinations(permutations[key], 3)):
            if b - a == c - b:
                yield (a, b, c)

if __name__ == "__main__":
    for (a, b, c) in get_arithmetic_sequences():
        if (a, b, c) != (1487, 4817, 8147):
            print(str(a) + str(b) + str(c))