from prime_sieve import PrimeSieve
import pytest

def test_get_primes():
    sieve = PrimeSieve(20)

    actual = list(sieve.get_primes())

    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    assert actual == expected;

def test_is_prime():
    sieve = PrimeSieve(10)

    assert sieve.is_prime(0) == False
    assert sieve.is_prime(1) == False
    assert sieve.is_prime(2) == True
    assert sieve.is_prime(3) == True
    assert sieve.is_prime(4) == False

def test_init_exclusive_till():
    sieve = PrimeSieve(5)

    assert sieve.is_prime(4) == False

    with pytest.raises(Exception):
        sieve.is_prime(5)