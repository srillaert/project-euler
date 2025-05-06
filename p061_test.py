from p061 import *

def test_get_figurate_numbers():
	generators = [ p4 ]
	actual = get_figurate_numbers(generators)
	assert actual[0] == (1024, 0)

def test_get_cyclical_figurate_numbers_from_list_simple():
	figurate_numbers = [(1122, 0), (2211, 1)]
	actual = get_cyclical_figurate_numbers_from_list(figurate_numbers)
	assert actual == [1122, 2211]

def test_get_cyclical_figurate_numbers_from_list_same_type():
	figurate_numbers = [(1122, 0), (2211, 0)]
	actual = get_cyclical_figurate_numbers_from_list(figurate_numbers)
	assert actual == None

def test_get_cyclical_figurate_numbers_from_list_too_short_cycle():
	figurate_numbers = [(1717, 0), (1234, 1)]
	actual = get_cyclical_figurate_numbers_from_list(figurate_numbers)
	assert actual == None

def test_get_cyclical_figurate_numbers_from_list_two_lookup_items():
	figurate_numbers = [(8128, 0), (2809, 1), (8281, 1), (2882, 2)] # 2809 and 2882 start both with 28
	actual = get_cyclical_figurate_numbers_from_list(figurate_numbers)
	assert actual == [2882, 8281, 8128]

def test__get_cyclical_figurate_numbers_from_list_example():
	generators = [ p3, p4, p5 ]
	figurate_numbers = get_figurate_numbers(generators)
	actual = get_cyclical_figurate_numbers_from_list(figurate_numbers)
	assert actual == [2882, 8281, 8128]