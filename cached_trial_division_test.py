from cached_trial_division import CachedTrialDivision
from itertools import islice

def test_get_primes():
    cache = CachedTrialDivision()

    actual = list(islice(cache.get_primes(), 5))

    expected = [2, 3, 5, 7, 11]
    assert(actual == expected)

def test_is_prime():
    cache = CachedTrialDivision()

    assert(cache.is_prime(2) == True)
    assert(cache.is_prime(3) == True)
    assert(cache.is_prime(4) == False)
    assert(cache.is_prime(9) == False)
    assert(cache.is_prime(11) == True)