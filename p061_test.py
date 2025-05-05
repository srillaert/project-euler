from p061 import *

def test_get_figurate_numbers():
	generators = [
		lambda n : n * (n + 1) // 2,
		lambda n : n * n,
		lambda n : n * (3 * n - 1) // 2
	]
	actual = get_figurate_numbers(generators)
	assert actual[0] == (1035, 0)

def test_get_cyclical_figurate_numbers_from_list_simple():
	figurative_numbers = [(1122, 0), (2211, 1)]
	actual = get_cyclical_figurate_numbers_from_list(figurative_numbers, 2)
	assert actual == [1122, 2211]

def test_get_cyclical_figurate_numbers_from_list_same_type():
	figurative_numbers = [(1122, 0), (2211, 0)]
	actual = get_cyclical_figurate_numbers_from_list(figurative_numbers, 2)
	assert actual == None

def test_get_cyclical_figurate_numbers_from_list_too_short_cycle():
	figurative_numbers = [(1717, 0), (1234, 1)]
	actual = get_cyclical_figurate_numbers_from_list(figurative_numbers, 2)
	assert actual == None

def test_get_cyclical_figurate_numbers_from_list_two_lookup_items():
	figurative_numbers = [(8128, 0), (2809, 1), (8281, 1), (2882, 2)]
	actual = get_cyclical_figurate_numbers_from_list(figurative_numbers, 3)
	assert actual == [2882, 8281, 8128]

def test__get_cyclical_figurate_numbers_from_list_example():
	generators = [
		lambda n : n * (n + 1) // 2,
		lambda n : n * n,
		lambda n : n * (3 * n - 1) // 2,
	]
	figurate_numbers = get_figurate_numbers(generators)
	actual = get_cyclical_figurate_numbers_from_list(figurate_numbers, 3)
	assert actual == [2882, 8281, 8128]