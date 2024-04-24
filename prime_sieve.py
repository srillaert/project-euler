from math import sqrt

class PrimeSieve:
    # Based on list_primality(n) of https://github.com/nayuki/Project-Euler-solutions/blob/master/python/eulerlib.py
    def __init__(self, exclusive_till):
        is_prime_list = [True] * (exclusive_till)
        is_prime_list[0] = is_prime_list[1] = False
        for i in range(int(sqrt(exclusive_till - 1)) + 1):
            if is_prime_list[i]:
                for j in range(i*i, exclusive_till, i):
                    is_prime_list[j] = False
        self.__is_prime_list = is_prime_list

    def get_primes(self):
        yield 2
        for n in range(3, len(self.__is_prime_list), 2):
            if self.__is_prime_list[n]:
                yield n
    
    def is_prime(self, n):
        return self.__is_prime_list[n]