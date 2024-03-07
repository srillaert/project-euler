from p004 import largest_product, largest_palindrome_product

def test_largest_product():
    parameters = []
    condition = lambda n : parameters.append(n) or (n == 49)
    result = largest_product(9, 0, condition)
    assert(result == 49)
    assert(parameters == [9*9, 8*9, 8*8, 7*9, 7*8, 7*7, 6*9])

def test_example():
    result = largest_palindrome_product(2)
    assert(result == 9009)