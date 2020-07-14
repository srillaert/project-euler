def trial_divisors():
	yield 2
	yield 3
	n = 5
	while True: # Odd numbers not divisible by 3
		yield n
		yield n + 2
		n += 6

def prime_factors(n):
	for d in trial_divisors():
		if d*d > n:
			break
		while n%d == 0:
			yield d
			n //= d
	if n != 1:
		yield n

def prime_factor_exponents(n):
    current_factor = 0
    count = 0
    for p in prime_factors(n):
        if p != current_factor and current_factor != 0:
            yield count
            count = 0
        current_factor = p
        count += 1
    yield count

def number_of_divisors(n):
    product = 1
    for e in prime_factor_exponents(n):
        product *= (e + 1)
    return product

count = 0
n = 0
i = 0
while count < 500:
    i += 1
    n += i
    count = number_of_divisors(n)
print(n)
