from itertools import takewhile
from math import floor, sqrt

class CachedTrialDivision:
    def __init__(self):
        self.cached_primes = [2, 3]
        self.last_checked = 3

    def get_primes(self, inclusive_till):
        for n in range(self.last_checked + 2, inclusive_till + 1, 2):
            square_root = floor(sqrt(n))
            primes_to_test = takewhile(lambda p: p <= square_root, self.cached_primes)
            if all(n % p != 0 for p in primes_to_test):
                self.cached_primes.append(n)
            self.last_checked = n

        return takewhile(lambda p: p <= inclusive_till, self.cached_primes)

    def is_prime(self, n):
        inclusive_till = floor(sqrt(n))
        return all(n % p != 0 for p in self.get_primes(inclusive_till))