# Based on the comment of Vlad on https://www.mathblog.dk/project-euler-49-arithmetic-sequences-primes-permutations/
from itertools import combinations
from prime import get_is_prime_array

till = 10000
is_prime_array = get_is_prime_array(till)

permutations = {}
for d in range(1000, till):
    if is_prime_array[d]:
        key = ''.join(sorted(str(d))) # Permutations get the same key
        value = permutations.get(key)
        if value == None:
            permutations[key] = [ d ]
        else:
            value.append(d)

for key in permutations:
    for a, b, c in sorted(combinations(permutations[key], 3)):
        if b - a == c - b and a != 1487:
            print(str(a) + str(b) + str(c))