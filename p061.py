# generator formulae
def p3(n): return n * (n + 1) // 2
def p4(n): return n * n
def p5(n): return n * (3 * n - 1) // 2
def p6(n): return n * (2 * n - 1)
def p7(n): return n * (5 * n - 3) // 2
def p8(n): return n * (3 * n - 2)

def get_figurate_numbers_helper(generator):
	n = 1
	while True:
		figurate_number = generator(n)
		if figurate_number >= 10000:
			break
		if figurate_number >= 1000:
			yield figurate_number
		n += 1

def get_figurate_numbers(generators):
	return [(n, i) for i, g in enumerate(generators) for n in get_figurate_numbers_helper(g)]

def get_cyclical_figurate_numbers(lookup, current, stop, visited_types):
	lookup_items = lookup.get(current%100)
	for lookup_item in lookup_items:
		n, figurate_type = lookup_item
		if n == stop:
			if all(visited_types):
				return [current]
			else:
				return None
		elif visited_types[figurate_type]:
			continue # we have already visited this type without reaching a cycle
		else:
			visited_types[figurate_type] = True
			result = get_cyclical_figurate_numbers(lookup, n, stop, visited_types)
			if result != None:
				result.append(current)
				return result
			visited_types[figurate_type] = False
	return None

def get_cyclical_figurate_numbers_from_list(figurate_numbers):
	types_count = max(figurate_type for _, figurate_type in figurate_numbers) + 1
	lookup = dict()
	for n in range(100):
		lookup[n] = []
	for n, figurate_type in figurate_numbers:
		lookup[n//100].append((n, figurate_type))

	for lookup_value in lookup.values():
		for start, figurate_type in lookup_value:
			visited_types = [False] * types_count
			visited_types[figurate_type] = True
			result = get_cyclical_figurate_numbers(lookup, start, start, visited_types)
			if result != None:
				result.reverse()
				return result
	return result

if __name__ == "__main__":
	generators = [ p3, p4, p5, p6, p7, p8 ]
	figurate_numbers = get_figurate_numbers(generators)
	cyclical_figurate_numbers = get_cyclical_figurate_numbers_from_list(figurate_numbers)
	solution = sum(cyclical_figurate_numbers)
	print(solution)