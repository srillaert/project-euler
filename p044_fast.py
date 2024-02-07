from math import sqrt

def pentagonal(n):
    return n * (3 * n - 1) // 2

## see https://en.wikipedia.org/wiki/Pentagonal_number#Tests_for_pentagonal_numbers
def is_pentagonal(n):
    r = sqrt(1 + 24 * n)
    return r % 6 == 5

def solution():
    pentagonals_til_now = [ pentagonal(1) ]
    k = 2
    while True:
        pk = pentagonal(k)
        for pj in pentagonals_til_now:
            if is_pentagonal(pk + pj) and is_pentagonal(pk - pj):
                return pk - pj
        pentagonals_til_now.insert(0, pk) # in front so that we can loop over the pentagonals from latest to oldest
        k += 1

print(solution())