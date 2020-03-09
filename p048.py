sum = 0
for i in range(1,1001):
	sum += i**i
remainder = sum % (10**10)
print(remainder)
