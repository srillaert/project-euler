from p003 import get_largest_prime_factor

def test_example():
    # The prime factors of 13195 are 5, 7, 13 and 29.
    result = get_largest_prime_factor(13195)
    assert(result == 29)