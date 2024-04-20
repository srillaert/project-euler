from p058 import get_square_spirals

def test_get_square_spirals_example():
    actual = next((primes_count, numbers_count, side_length)
                  for (primes_count, numbers_count, side_length) in get_square_spirals()
                  if side_length == 7)

    expected = (8, 13 ,7)
    assert(actual == expected)