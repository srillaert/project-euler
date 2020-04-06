from prime import is_prime

def find_largest_pandigital_prime(used_digits, n):
	for i in range(len(used_digits)-1, -1, -1):
		if used_digits[i]:
			continue;
		m = n * 10 + i + 1
		if m > 10 ** (len(used_digits) - 1):
			if is_prime(m):
				return m
			else:
				return -1
		else:
			used_digits[i] = True
			result = find_largest_pandigital_prime(used_digits, m)
			if result != -1:
				return result
			used_digits[i] = False
	return -1

for n in range(9, 0, -1):
	used_digits = [False] * n
	result = find_largest_pandigital_prime(used_digits, 0)
	if result != -1:
		break
print(result)
