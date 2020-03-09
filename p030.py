def is_sum_powers_of_digits(n, power):
	quotient = n
	sum = 0
	while quotient > 0:
		sum += (quotient % 10) ** power
		quotient //= 10
	return sum==n

sum_solutions = 0
till = (9**5)*5
for n in range(10, till):
	if is_sum_powers_of_digits(n, 5):
		sum_solutions += n
print(sum_solutions)
