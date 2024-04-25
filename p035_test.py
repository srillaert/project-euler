from p035 import get_circular_prime_count, is_circular_prime
from prime_sieve import PrimeSieve
import pytest

problem_examples_circular_primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 197]
@pytest.mark.parametrize("n", problem_examples_circular_primes)
def test_is_circular_prime(n):
	sieve = PrimeSieve(1000) # A rotation of 197 is 971
	assert(is_circular_prime(sieve, n))

def test_get_circular_prime_count():
	# Example from the problem : 13 circular primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
	assert get_circular_prime_count(100) == 13