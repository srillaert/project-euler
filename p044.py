from math import sqrt

def pentagonal(n):
    return n * (3 * n - 1) // 2

## see https://en.wikipedia.org/wiki/Pentagonal_number#Tests_for_pentagonal_numbers
def is_pentagonal(n):
    r = sqrt(1 + 24 * n);
    return r % 6 == 5;

def solution():
    k = 2
    while True:
        pk = pentagonal(k)
        for j in range(k-1, 0, -1):
            pj = pentagonal(j)
            #print(k, j)
            if is_pentagonal(pk + pj) and is_pentagonal(pk - pj):
                return pk - pj
        k += 1

print(solution())