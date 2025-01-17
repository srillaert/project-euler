from p500 import *

def test_get_factors():
	assert list(get_factors(100, 7)) == [2, 3, 4, 5, 7, 9, 11]

def test_get_smallest_number_with_power_of_2_divisors():
	assert get_smallest_number_with_power_of_2_divisors(100, 3) == 24
	assert get_smallest_number_with_power_of_2_divisors(100, 4) == 120
	assert get_smallest_number_with_power_of_2_divisors(100, 5) == 840
	assert get_smallest_number_with_power_of_2_divisors(100, 6) == 7560