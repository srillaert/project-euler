from p918 import *

def test_calculate_an():
	actual = list(calculate_an(n) for n in range(1, 11))
	assert actual == [1, 2, -5, 4, 17, -10, -17, 8, -47, 34]

def test_calculate_s():
	assert calculate_s(10) == -13