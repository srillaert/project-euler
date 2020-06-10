from itertools import count

def get_least_common_multiple_fast(to):
    quotients = list(range(to + 1))
    result = 1
    for i in range(2, len(quotients)):
        result *= quotients[i]
        for j in range(2 * i, len(quotients), i):
            quotients[j] //= quotients[i]
    return result

def get_least_common_multiple_slow(to):
    for n in count(1):
        if all(n % d == 0 for d in range(1, to + 1)):
            return n

def test_compare_with_slow():
    for i in range(1, 11):
        assert get_least_common_multiple_slow(i) == get_least_common_multiple_fast(i)

def test_example():
    assert get_least_common_multiple_fast(10) == 2520

if __name__ == "__main__":
    print(get_least_common_multiple_fast(20))
