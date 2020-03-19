from math import sqrt

def is_prime(n):
	if n == 2:
		return True
	if n%2 == 0:
		return False
	till = int(sqrt(n))
	for i in range(3, till+1, 2):
		if n%i == 0:
			return False
	return True
