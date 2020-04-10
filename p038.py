def concatenated_products():
	for number in range(1, 9877):
		multiplier = 1
		concatenation = str(number)
		while len(concatenation) < 9:
			multiplier += 1
			concatenation += str(number * multiplier)
		yield concatenation

largest = max(cp for cp in concatenated_products() if sorted(cp) == sorted("123456789"))
print(largest)
