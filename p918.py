def calculate_an(n):
	if n == 1:
		return 1
	elif n % 2 == 0:
		return 2 * calculate_an(n // 2)
	else:
		half = n // 2
		return calculate_an(half) - 3 * calculate_an(half + 1)

def calculate_s(n):
	return 4 - calculate_an(n/2)

if __name__ == "__main__":
	solution = calculate_s(10**12)
	print(solution)