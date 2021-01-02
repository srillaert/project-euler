def gcd(a, b):
    if b > a:
        a, b = b, a
    while(b != 0):
        a, b = b, a % b
    return a

def test_gcd():
    assert gcd(9, 8) == 1
    assert gcd(9, 6) == 3

numerator = 1
denominator = 1
for a in range(1, 10):
	for b in range(a + 1, 10): # ab/bc < 1
		for c in range(1, 10):
			if ((10.0 * a + b) * c) / (10.0 * b + c) == a: # test whether ab/bc == a/c
				numerator *= a
				denominator *= c
result = denominator // gcd(numerator, denominator)
print(result)
