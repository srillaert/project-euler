from math import ceil, sqrt

def get_factors(n):
	till = ceil(sqrt(n))
	d = 2
	while d <= till:
		if n % d == 0:
			yield d
		while n % d == 0:
			n //= d
		till = ceil(sqrt(n))
		d += 1
	if n != 1:
		yield n

def numerator_just_above(d):
	return (d + 3) // 3
	
def numerator_just_below(d):
	return (d - 1) // 2

till_d = 12000
result = 0
for d in range(2, till_d + 1):
	factors = list(get_factors(d))
	from_n = numerator_just_above(d)
	to_n = numerator_just_below(d)
	for n in range(from_n, to_n + 1):
		if all(n % f != 0 for f in factors):
			result += 1
print(result)