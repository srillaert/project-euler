from math import factorial

def binomial_coefficient(n, r):
	return factorial(n) // (factorial(r) * factorial(n-r))

count = sum(1 for n in range(23,101) for r in range(1,n) if binomial_coefficient(n, r) > 10 ** 6)
print(count)
