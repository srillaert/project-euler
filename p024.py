from math import factorial

def get_lexicographic_permutation(digits_count, position):
	digits = [str(i) for i in range(0, digits_count)]
	result = ""
	for i in range(digits_count-1, -1, -1):
		permutations_count = factorial(i)
		index = (position - 1) // permutations_count
		digit = digits.pop(index)
		result += digit
		position -= index * permutations_count
	return result

result = get_lexicographic_permutation(10, 10**6)
print(result)
