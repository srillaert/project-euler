from math import floor, log10

def calculate_p(L, n):
	power_of_10 = pow(10, floor(log10(L)))
	base_L = L / power_of_10
	min, max = log10(base_L), log10(base_L + 1 / power_of_10)
	digits_log = log10_of_2 = log10(2)
	power = 1
	while True:
		if digits_log >= min and digits_log < max:
			n -= 1
			if (n == 0):
				return power
		power += 1
		digits_log = (digits_log + log10_of_2) % 1

if __name__ == "__main__":
	solution = calculate_p(123, 678910)
	print(solution)