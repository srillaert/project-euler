from functools import reduce # Valid in Python 2.6+, required in Python 3, from https://stackoverflow.com/questions/595374/whats-the-function-like-sum-but-for-multiplication-product
import operator

def get_greatest_product(length):
    with open("p008.input") as input_file:
        digits = list(int(c) for c in input_file.read().replace("\n", ""))
    greatest_product = max(reduce(operator.mul, digits[i:i+length], 1) for i in range(1000-length))
    return greatest_product

def test_example():
    assert get_greatest_product(4) == 5832

if __name__ == "__main__":
    greatest_product = get_greatest_product(13)
    print(greatest_product)