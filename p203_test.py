from p203 import *

def test_get_prime_factors():
	actual = get_prime_factors(20)

	expected = [0] * len(primes)
	expected[0] = 2
	expected[2] = 1

	assert actual == expected

def test_is_square_free():
	factorial_factors = get_factorial_factors(7)
	assert not is_square_free(factorial_factors, 4, 1)
	assert is_square_free(factorial_factors, 4, 2)
	assert not is_square_free(factorial_factors, 4, 3)

	assert is_square_free(factorial_factors, 6, 2)
	assert not is_square_free(factorial_factors, 6, 3)


def test_get_solution_example():
	actual = get_solution(8)

	assert actual == 105