from itertools import count, takewhile
from math import floor, sqrt

class CachedTrialDivision:
    def __init__(self):
        self.cached_primes = [2, 3]

    def get_primes(self):
        last_p = 3
        for p in self.cached_primes:
            last_p = p
            yield p
        for n in count(last_p + 2, 2):
            till = floor(sqrt(n))
            primes_to_test = takewhile(lambda p: p <= till, self.cached_primes)
            if all(n % p != 0 for p in primes_to_test):
                self.cached_primes.append(n)
                yield n

    def is_prime(self, n):
        till = floor(sqrt(n))
        primes_to_test = takewhile(lambda p: p <= till, self.get_primes())
        return all(n % p != 0 for p in primes_to_test)