from prime import get_is_prime_array

step = 3330
till = 10000
is_prime_array = get_is_prime_array(till)

for i in range(1001, till - 2 * step, 2):
	if is_prime_array[i] and is_prime_array[i+step] and is_prime_array[i+2*step]:
		if sorted(str(i)) == sorted(str(i+step)) == sorted(str(i+2*step)):
			if i != 1487:
				print(str(i) + str(i+step) + str(i+2*step))
