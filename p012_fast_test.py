from itertools import islice
from p012_fast import *

def test_get_triangle_numbers():
    actual = list(islice(get_triangle_numbers(), 10))
    expected = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    assert actual == expected

def test_get_solution_example():
    actual = get_solution(5)
    assert actual == 28 # 28 is the first triangle number to have over five divisors