def sum_digits(n):
	return sum(int(d) for d in str(n))

result = max(sum_digits(a**b) for a in range(1,100) for b in range(1,100))
print(result)
