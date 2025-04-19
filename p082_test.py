from p082 import *

def test_get_minimal_path_sum_down():
    matrix = [
        [1,1,4],
        [3,1,3],
        [4,1,1]
    ]
    assert get_minimal_path_sum(matrix) == 5

def test_get_minimal_path_sum_up():
    matrix = [
        [4,1,1],
        [3,1,3],
        [1,1,4]
    ]
    assert get_minimal_path_sum(matrix) == 5

def test_get_minimal_path_sum_from_file_example():
	actual = get_minimal_path_sum_from_file("p082_example.input")
	assert actual == 994