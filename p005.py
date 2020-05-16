def get_smallest_multiple(to):
    quotients = list(range(2, to + 1))
    result = 1
    for i in range(len(quotients)):
        divisor = quotients[i]
        if divisor == 1:
            continue
        for j in range(2 * i + 2, len(quotients), i + 2):
            quotients[j] //= divisor
        result *= divisor
    return result

def test_example():
    assert get_smallest_multiple(10) == 2520

if __name__ == "__main__":
    print(get_smallest_multiple(20))
