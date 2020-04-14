from prime import get_is_prime_array

is_prime_array = get_is_prime_array(1000000)

def confirms_conjecture(n):
	j = 1
	while True:
		difference = n - 2 * j * j
		if difference < 2:
			return False
		if is_prime_array[difference]:
			return True
		j += 1

n = 7
while True:
	n += 2
	if is_prime_array[n]:
		continue
	if not confirms_conjecture(n):
		break
print(n)
