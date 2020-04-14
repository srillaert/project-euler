def get_available_digit(number):
	is_digit_used = [False] * 10
	for i in range(9):
		digit = number % 10
		if is_digit_used[digit]:
			return -1 # not a pandigital number
		is_digit_used[digit] = True
		number //= 10
	for i in range(10):
		if not is_digit_used[i]:
			return i

def is_substring_not_divisible(number, power_of_ten, divisor):
	return ((number // (10 ** power_of_ten)) % 1000) % divisor != 0

result = 0
for right in range(17, 1000, 17):
	for middle in range(14, 1000, 7):
		number = middle * 1000 + right
		if is_substring_not_divisible(number, 1, 13):
			continue
		if is_substring_not_divisible(number, 2, 11):
			continue
		for left in range(12, 1000, 2):
			number = left * 1000000 + middle * 1000 + right
			if is_substring_not_divisible(number, 4, 5):
				continue
			if is_substring_not_divisible(number, 5, 3):
				continue
			digit = get_available_digit(number)
			if digit != -1:
				result += digit * 1000000000 + number
print(result)
