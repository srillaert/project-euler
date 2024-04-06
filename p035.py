# Based on https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p035.py
import pytest
from prime import get_is_prime_array

till = 10**6
is_prime = get_is_prime_array(till)

def is_circular_prime(n):
	str_n = str(n)
	return all(is_prime[int(str_n[i:] + str_n[:i])] for i in range(len(str_n)))

problem_examples_circular_primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 197]
@pytest.mark.parametrize("n", problem_examples_circular_primes)
def test_is_circular_prime(n):
	assert(is_circular_prime(n))

def get_circular_prime_count(till):
	count = sum(1 for n in range(till) if is_circular_prime(n))
	return count

def test_get_circular_prime_count():
	# Example from the problem : 13 circular primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
	assert get_circular_prime_count(100) == 13

if __name__ == "__main__":
	result = sum(1 for n in range(till) if is_circular_prime(n))
	print(result)
