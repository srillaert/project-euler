from prime import get_is_prime_array

max_count = 6
prime_sum = 41
till = 1000000

is_prime_array = get_is_prime_array(till)

def get_next_prime(current):
	result = current + 1
	while not is_prime_array[result]:
		result += 1
	return result

current_start = 2
while current_start <= (till // max_count):
	prime = current_start
	current_sum = current_start
	count = 1
	while current_sum < till:
		if count > max_count and is_prime_array[current_sum]:
			max_count = count
			prime_sum = current_sum
		prime = get_next_prime(prime)
		current_sum += prime
		count += 1
	current_start = get_next_prime(current_start)

print(prime_sum)
