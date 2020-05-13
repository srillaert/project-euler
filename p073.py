from prime import get_factors

till_d = 12000
result = 0
for d in range(2, till_d + 1):
	factors = list(get_factors(d))
	from_n = (d // 3) + 1
	to_n = (d - 1) // 2
	for n in range(from_n, to_n + 1):
		if all(n % f != 0 for f in factors):
			result += 1
print(result)