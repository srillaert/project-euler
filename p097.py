modulo_divisor = 10 ** 10
number = 1
for i in range(7830457):
	number = (number * 2) % modulo_divisor
number = ((28433 * number) + 1) % modulo_divisor
print(number)
