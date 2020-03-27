from prime import get_is_prime_array

till = 10**6
is_prime = get_is_prime_array(till)

result = 1
for n in range(3, till, 2):
	if is_prime[n]:
		rotate = str(n)
		all_prime = True
		while all_prime:
			rotate = rotate[-1] + rotate[0:-1]
			int_rotate = int(rotate)
			if is_prime[int_rotate] == False:
				all_prime = False
			if int_rotate == n:
				break
		if all_prime:
			result += 1
print(result)
