from prime import get_primes

def get_indexed_prime(index):
    primes = get_primes()
    return next(x for i,x in enumerate(primes) if i == index)

def test_get_indexed_prime():
    assert get_indexed_prime(5) == 13

if __name__ == "__main__":
    result = get_indexed_prime(10000)
    print(result)
