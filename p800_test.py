from p800 import *

def test_get_number_hybrid_integers():
	first_ordered_hybrid_integers = [
		72, # 2**3 * 3**2
		800, # 2**5 * 5**2
		6272, # 2**7 * 7**2
		30375, # 3**5 * 5**3
		247808, # 2**11 * 11**2
	]
	for i in range(len(first_ordered_hybrid_integers)):
		assert get_number_hybrid_integers(first_ordered_hybrid_integers[i] - 1, 1) == i
		assert get_number_hybrid_integers(first_ordered_hybrid_integers[i], 1) == i + 1

def test_get_number_hybrid_integers_exponent():
	assert get_number_hybrid_integers(6, 6) == 4 # 6**6 == 46656

def test_solution_examples():
	assert get_number_hybrid_integers(800, 1) == 2
	assert get_number_hybrid_integers(800, 800) == 10790