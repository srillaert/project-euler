from p686 import *

def test_calculate_p_examples():
	assert calculate_p(12, 1) == 7
	assert calculate_p(12, 2) == 80
	assert calculate_p(123, 45) == 12710