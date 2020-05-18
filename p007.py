from prime import is_prime

def get_primes():
    yield 2
    yield 3
    n = 5
    while True:
        if is_prime(n):
            yield n
        if is_prime(n + 2):
            yield n + 2
        n += 6

def get_indexed_prime(index):
    primes = get_primes()
    return next(x for i,x in enumerate(primes) if i == index)

def test_get_indexed_prime():
    assert get_indexed_prime(5) == 13

if __name__ == "__main__":
    result = get_indexed_prime(10000)
    print(result)
