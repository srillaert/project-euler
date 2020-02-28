factorial = 1
for i in range(1, 101):
	factorial *= i
sum_digits = 0
while factorial > 0:
	sum_digits += (factorial % 10)
	factorial //= 10
print(sum_digits)
