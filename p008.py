from functools import reduce # Valid in Python 2.6+, required in Python 3, from https://stackoverflow.com/questions/595374/whats-the-function-like-sum-but-for-multiplication-product
import operator

def get_greatest_product_list(digits, number_of_adjacent_digits):
    greatest_product = max(
        reduce(operator.mul, digits[i:i+number_of_adjacent_digits], 1)
        for i in range(len(digits) - number_of_adjacent_digits + 1))
    return greatest_product

def test_get_greatest_product_list_at_start():
    digits = list(reversed(range(4)))
    result = get_greatest_product_list(digits, 2)
    assert result == 3 * 2

def test_get_greatest_product_list_at_end():
    digits = list(range(4))
    result = get_greatest_product_list(digits, 2)
    assert result == 2 * 3

def get_digits_from_file():
    with open("p008.input") as input_file:
        digits = list(int(c) for c in input_file.read().replace("\n", ""))
    return digits

def test_get_digits_from_file():
    digits = get_digits_from_file()
    assert len(digits) == 1000 # problem description: file contains 1000 digit number

def get_greatest_product_file(number_of_adjacent_digits):
    digits = get_digits_from_file()
    return get_greatest_product_list(digits, number_of_adjacent_digits)

def test_example():
    assert get_greatest_product_file(4) == 5832

if __name__ == "__main__":
    solution = get_greatest_product_file(13)
    print(solution)