from prime import get_primes

def get_nth_prime(n):
    primes = get_primes()
    return next(x for i,x in enumerate(primes) if i == (n - 1))

def test_get_nth_prime():
    assert get_nth_prime(6) == 13

if __name__ == "__main__":
    result = get_nth_prime(10001)
    print(result)
