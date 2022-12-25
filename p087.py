from prime import get_primes

def number_below(till):
    values = set()
    for z in get_primes():
        power4 = z**4
        if (power4 >= till):
            break
        for y in get_primes():
            power3 = y**3
            if (power3 >= till):
                break
            for x in get_primes():
                power2 = x**2
                sum = power4 + power3 + power2
                if (sum >= till):
                    break
                values.add(sum)
    count = len(values)
    return count

def test_example():
    assert number_below(50) == 4

if __name__ == "__main__":
    print(number_below(50000000))