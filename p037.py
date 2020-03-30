import math, prime

def remove_left_to_right(n):
	log = int(math.log10(n))
	for i in range(log, 0, -1):
		yield n % 10 ** i

def remove_right_to_left(n):
	while True:
		n //= 10
		if n == 0:
			break
		yield n

till = 1000000
is_prime = prime.get_is_prime_array(till)

result = 0
for n in range(11, till, 2):
	if is_prime[n]:
		if all(is_prime[m] for m in remove_left_to_right(n)):
			if all(is_prime[m] for m in remove_right_to_left(n)):
				result += n
print(result)
