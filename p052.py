def equal_digits_count(a, b):
	return all(a[i] == b[i] for i in range(10))

def get_digits_count(n):
	digits_count = [0] * 10
	while n>0:
		digit = n%10
		digits_count[digit] += 1
		n //= 10
	return digits_count

number = 0
is_equal = False
while not is_equal:
	number += 1
	digits_count_number = get_digits_count(number)
	for multiple in range(2*number, 7*number, number):		
		digits_count_multiple = get_digits_count(multiple)
		is_equal = equal_digits_count(digits_count_number, digits_count_multiple)
		if not is_equal:
			break
print(number)
