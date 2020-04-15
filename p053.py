from math import factorial

def combinatoric_selections(n, r):
	return factorial(n) // (factorial(r) * factorial(n-r))

count = 0
for n in range(23,101):
	for r in range(1,n):
		if combinatoric_selections(n, r) > 10 ** 6:
			count += 1
print(count)
