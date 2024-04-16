from itertools import islice
from p050 import get_consecutive_primes, get_next_prime, get_solution
from prime import get_is_prime_array

def test_get_next_prime():
    is_prime_array = get_is_prime_array(20)
    assert(get_next_prime(2, is_prime_array) == 3)
    assert(get_next_prime(3, is_prime_array) == 5)
    assert(get_next_prime(7, is_prime_array) == 11)

def test_get_consecutive_primes():
    is_prime_array = get_is_prime_array(10)
    actual = list(islice(get_consecutive_primes(2, is_prime_array), 3))
    assert(actual == [2, 3, 5])

def test_get_solution_examples():
    assert(get_solution(100) == 41)
    assert(get_solution(1000) == 953)