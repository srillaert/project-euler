from itertools import islice
from prime_sieve import PrimeSieve

def get_solution():
    # for how to calculate an upper bound, see the answer on https://math.stackexchange.com/questions/54312/non-trivial-upper-bound-for-the-number-of-primes-less-or-equal-to-n
    # for n = 105000 : (n / log(n)) * (1 + 1.2762/log(n)) == 10084.14889762712, more than 10001 so this is a good upper bound
    upper_bound = 105000
    sieve = PrimeSieve(upper_bound)
    primes = sieve.get_primes()
    result = next(islice(primes, 10000, 10001)) # Use itertools.islice to get the 10001st element
    return result

if __name__ == "__main__":
    solution = get_solution()
    print(solution)