from p037 import get_truncations, get_truncatable_primes

def test_get_truncations_example():
    result = list(get_truncations(3797))
    assert sorted(result) == sorted([3797, 797, 97, 7, 379, 37, 3])

def test_get_truncatable_primes_example():
    count = sum(1 for _ in get_truncatable_primes())
    assert count == 11 # problem statement : only eleven primes that are both truncatable from left to right and right to left