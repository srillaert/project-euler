from prime import is_prime

def is_counterexample(n):
	j = 1
	while True:
		difference = n - 2 * j * j
		if difference < 2:
			return True
		if is_prime(difference):
			return False
		j += 1

n = 9
while is_prime(n) or not is_counterexample(n):
	n += 2
print(n)
