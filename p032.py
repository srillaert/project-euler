def is_pandigital(n):
	if n < 10**8 or n > 10**9: # outside of the range of 9 digit numbers
		return False
	# make sure the number contains unique digits 1 to 9
	has_digit = [False] * 9
	while n > 0:
		digit = n % 10
		if digit == 0 or has_digit[digit-1]:
			return False
		has_digit[digit-1] = True
		n //= 10
	return True

products = []
for n in range(12345, 98765 + 1):
	product = (n // 1000) * (n % 1000)
	if is_pandigital(product * 100000 + n):
		products.append(product)
	product = (n // 10000) * (n % 10000)
	if is_pandigital(product * 100000 + n):
		products.append(product)

result = sum(n for n in set(products))
print(result)
