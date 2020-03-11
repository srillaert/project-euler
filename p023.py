from math import ceil, sqrt

upper_limit = 28123

def get_proper_divisors(n):
	yield 1
	sqrtn = ceil(sqrt(n))
	for i in range(2, sqrtn):
		if n%i == 0:
			yield i
			yield n//i
	if sqrtn*sqrtn == n:
		yield sqrtn

def is_abundant_number(n):
	sum_divisors = sum(get_proper_divisors(n))
	return sum_divisors > n

abundant_numbers = []
for i in range(2, upper_limit + 1):
	if(is_abundant_number(i)):
		abundant_numbers.append(i)

is_sum_two_abundant_numbers = [False] * upper_limit

for i in range(0, len(abundant_numbers)):
	for j in range(i, len(abundant_numbers)):
		sum_two_abundant_numbers = abundant_numbers[i] + abundant_numbers[j]
		if sum_two_abundant_numbers > upper_limit:
			break
		is_sum_two_abundant_numbers[sum_two_abundant_numbers - 1] = True

result = 0
for i in range(0, upper_limit):
	if is_sum_two_abundant_numbers[i] == False:
		result += (i+1)

print(result)
