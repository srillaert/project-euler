from itertools import count
from math import sqrt

def pentagonal(n):
    return n * (3 * n - 1) // 2

## see https://en.wikipedia.org/wiki/Pentagonal_number#Tests_for_pentagonal_numbers
def is_pentagonal(n):
    r = sqrt(1 + 24 * n)
    return r % 6 == 5

def solution():
    pentagonals_til_now = []
    for k in count(1):
        pk = pentagonal(k)
        for pj in reversed(pentagonals_til_now):
            if is_pentagonal(pk + pj) and is_pentagonal(pk - pj):
                return pk - pj
        pentagonals_til_now.append(pk)

print(solution())