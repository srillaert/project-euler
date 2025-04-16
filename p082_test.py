from p082 import *

def test_minimal_path_sum_down():
    matrix = [
        [1,1,4],
        [3,1,3],
        [4,1,1]
    ]
    assert minimal_path_sum(matrix) == 5

def test_minimal_path_sum_up():
    matrix = [
        [4,1,1],
        [3,1,3],
        [1,1,4]
    ]
    assert minimal_path_sum(matrix) == 5
