from p050 import get_primes_from_is_prime_array, get_solution
from prime import get_is_prime_array

def test_get_primes_from_is_prime_array():
    is_prime_array = get_is_prime_array(10)
    actual = list(get_primes_from_is_prime_array(is_prime_array))
    assert(actual == [2, 3, 5, 7])

def test_get_solution_examples():
    assert(get_solution(100) == 41)
    assert(get_solution(1000) == 953)